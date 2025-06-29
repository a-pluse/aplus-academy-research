from flask import Blueprint, request, jsonify, send_file
from src.models.study import Study, db
from src.services.content_generator import AcademicContentGenerator
import json
import io
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

api_bp = Blueprint('api', __name__)
content_generator = AcademicContentGenerator()

@api_bp.route('/generate', methods=['POST'])
def generate_content():
    """API endpoint لتوليد المحتوى الأكاديمي"""
    try:
        data = request.get_json()
        section = data.get('section')
        study_data = data.get('data', {})
        
        if not section:
            return jsonify({'success': False, 'error': 'Section is required'}), 400
        
        # توليد المحتوى
        generated_content = content_generator.generate_content(section, study_data)
        
        # حفظ أو تحديث الدراسة في قاعدة البيانات
        study = None
        if 'study_id' in study_data:
            study = Study.query.get(study_data['study_id'])
        
        if not study and section == 'setup':
            # إنشاء دراسة جديدة
            study = Study(
                study_type=study_data.get('studyType'),
                field_of_study=study_data.get('fieldOfStudy'),
                main_topic=study_data.get('mainTopic'),
                problem_description=study_data.get('problemDescription'),
                keywords=study_data.get('keywords')
            )
            db.session.add(study)
            db.session.commit()
            study_data['study_id'] = study.id
        
        # حفظ المحتوى المولد
        if study and section != 'setup':
            setattr(study, f'{section}_content', generated_content)
            study.add_completed_section(section)
            
            # حفظ المدخلات الإضافية
            additional_inputs = study.get_additional_inputs()
            if f'{section}_input' in study_data:
                additional_inputs[f'{section}_input'] = study_data[f'{section}_input']
                study.set_additional_inputs(additional_inputs)
            
            db.session.commit()
        
        return jsonify({
            'success': True,
            'content': generated_content,
            'study_id': study.id if study else None
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@api_bp.route('/export', methods=['POST'])
def export_study():
    """API endpoint لتصدير الدراسة كملف PDF"""
    try:
        data = request.get_json()
        study_data = data.get('data', {})
        sections = data.get('sections', [])
        
        study_id = study_data.get('study_id')
        if not study_id:
            return jsonify({'success': False, 'error': 'Study ID is required'}), 400
        
        study = Study.query.get(study_id)
        if not study:
            return jsonify({'success': False, 'error': 'Study not found'}), 404
        
        # إنشاء ملف PDF
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72,
                              topMargin=72, bottomMargin=18)
        
        # تحضير المحتوى
        story = []
        styles = getSampleStyleSheet()
        
        # إضافة عنوان الدراسة
        if study.title_content:
            story.append(Paragraph("عنوان الدراسة", styles['Heading1']))
            story.append(Paragraph(study.title_content, styles['Normal']))
            story.append(Spacer(1, 12))
        
        # إضافة الملخص
        if study.abstract_content:
            story.append(Paragraph("الملخص", styles['Heading1']))
            story.append(Paragraph(study.abstract_content, styles['Normal']))
            story.append(Spacer(1, 12))
        
        # إضافة باقي الأقسام
        section_titles = {
            'introduction': 'المقدمة',
            'literature': 'الإطار النظري والدراسات السابقة',
            'methodology': 'منهجية الدراسة',
            'results': 'النتائج',
            'discussion': 'المناقشة',
            'conclusion': 'الخلاصة والتوصيات',
            'references': 'المراجع'
        }
        
        for section in sections:
            if section in section_titles:
                content = getattr(study, f'{section}_content', None)
                if content:
                    story.append(Paragraph(section_titles[section], styles['Heading1']))
                    # تنظيف المحتوى من HTML tags
                    clean_content = content.replace('<h3>', '').replace('</h3>', '')
                    clean_content = clean_content.replace('<p>', '').replace('</p>', '\n')
                    clean_content = clean_content.replace('<strong>', '').replace('</strong>', '')
                    clean_content = clean_content.replace('<em>', '').replace('</em>', '')
                    story.append(Paragraph(clean_content, styles['Normal']))
                    story.append(Spacer(1, 12))
        
        # بناء PDF
        doc.build(story)
        buffer.seek(0)
        
        return send_file(
            buffer,
            as_attachment=True,
            download_name=f'academic_study_{study.id}.pdf',
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@api_bp.route('/study/<int:study_id>', methods=['GET'])
def get_study(study_id):
    """الحصول على بيانات دراسة محددة"""
    try:
        study = Study.query.get(study_id)
        if not study:
            return jsonify({'success': False, 'error': 'Study not found'}), 404
        
        return jsonify({
            'success': True,
            'study': study.to_dict()
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@api_bp.route('/studies', methods=['GET'])
def get_studies():
    """الحصول على قائمة جميع الدراسات"""
    try:
        studies = Study.query.order_by(Study.created_at.desc()).all()
        return jsonify({
            'success': True,
            'studies': [study.to_dict() for study in studies]
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@api_bp.route('/study/<int:study_id>', methods=['DELETE'])
def delete_study(study_id):
    """حذف دراسة محددة"""
    try:
        study = Study.query.get(study_id)
        if not study:
            return jsonify({'success': False, 'error': 'Study not found'}), 404
        
        db.session.delete(study)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Study deleted successfully'})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

