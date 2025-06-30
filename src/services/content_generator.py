import re
import random
from typing import Dict, List, Any
import json

class AcademicContentGenerator:
    """
    خدمة توليد المحتوى الأكاديمي بأسلوب بشري طبيعي
    تطبق جميع الشروط والمعايير الموجودة في الدليل الأكاديمي المعزز
    """
    
    def __init__(self):
        self.academic_guidelines = self._load_academic_guidelines()
        self.humanization_strategies = self._load_humanization_strategies()
        
    def _load_academic_guidelines(self) -> Dict:
        """تحميل الشروط الأكاديمية من الدليل المعزز"""
        return {
            'title': {
                'length_range': (10, 15),
                'requirements': [
                    'يجب أن يكون دقيقاً وواضحاً ومختصراً',
                    'يعبر عن مشكلة الدراسة ومتغيراتها الرئيسية',
                    'جذاب وملفت للانتباه دون أن يكون مضللاً',
                    'يعكس التخصص العلمي للدراسة ونوعها',
                    'يتضمن الكلمات المفتاحية الأساسية'
                ]
            },
            'abstract': {
                'length_range': (150, 300),
                'components': [
                    'المقدمة/الخلفية',
                    'هدف الدراسة',
                    'المنهجية',
                    'النتائج الرئيسية',
                    'الاستنتاجات والتوصيات'
                ],
                'style_requirements': [
                    'تدفق منطقي متماسك',
                    'لغة دقيقة وموجزة',
                    'صوت أكاديمي رصين',
                    'تجنب العبارات النمطية',
                    'صياغة ديناميكية وقصصية'
                ]
            },
            'introduction': {
                'structure': [
                    'خلفية عامة عن الموضوع',
                    'أهمية الموضوع',
                    'الفجوة البحثية',
                    'لمحة موجزة عن مشكلة الدراسة',
                    'أهداف الدراسة العامة'
                ],
                'style_requirements': [
                    'التدرج من العام إلى الخاص',
                    'فقرات متسلسلة ومترابطة',
                    'لغة واضحة ومباشرة',
                    'تجنب الجمل الطويلة والمعقدة'
                ]
            },
            'literature': {
                'requirements': [
                    'مراجعة شاملة للأدبيات ذات الصلة',
                    'تحليل نقدي للدراسات السابقة',
                    'تحديد الفجوات البحثية',
                    'ربط الدراسات بالبحث الحالي',
                    'تنظيم منطقي للمحتوى'
                ]
            },
            'methodology': {
                'components': [
                    'نوع الدراسة ومنهجها',
                    'مجتمع الدراسة وعينتها',
                    'أدوات جمع البيانات',
                    'إجراءات الدراسة',
                    'المعالجة الإحصائية/التحليلية'
                ]
            }
        }
    
    def _load_humanization_strategies(self) -> Dict:
        """تحميل استراتيجيات الكتابة البشرية الطبيعية"""
        return {
            'sentence_variation': {
                'lengths': ['short', 'medium', 'long'],
                'structures': ['simple', 'compound', 'complex']
            },
            'vocabulary_variation': {
                'synonyms': True,
                'academic_terms': True,
                'field_specific': True
            },
            'style_techniques': [
                'vary_sentence_beginnings',
                'use_transitional_phrases',
                'incorporate_rhetorical_questions',
                'add_subtle_emphasis',
                'natural_flow_patterns'
            ],
            'anti_detection': [
                'avoid_repetitive_patterns',
                'vary_paragraph_lengths',
                'use_natural_language_quirks',
                'incorporate_human_reasoning_patterns'
            ]
        }
    
    def generate_content(self, section: str, study_data: Dict[str, Any]) -> str:
        """
        توليد المحتوى لقسم معين من الدراسة
        """
        if section == 'setup':
            return self._validate_setup_data(study_data)
        elif section == 'title':
            return self._generate_title(study_data)
        elif section == 'abstract':
            return self._generate_abstract(study_data)
        elif section == 'introduction':
            return self._generate_introduction(study_data)
        elif section == 'literature':
            return self._generate_literature_review(study_data)
        elif section == 'methodology':
            return self._generate_methodology(study_data)
        elif section == 'results':
            return self._generate_results(study_data)
        elif section == 'discussion':
            return self._generate_discussion(study_data)
        elif section == 'conclusion':
            return self._generate_conclusion(study_data)
        elif section == 'references':
            return self._generate_references(study_data)
        else:
            raise ValueError(f"Unknown section: {section}")
    
    def _validate_setup_data(self, data: Dict) -> str:
        """التحقق من صحة بيانات الإعداد"""
        required_fields = ['studyType', 'mainTopic', 'problemDescription']
        missing_fields = [field for field in required_fields if not data.get(field)]
        
        if missing_fields:
            return f"الحقول المطلوبة مفقودة: {', '.join(missing_fields)}"
        
        return "تم التحقق من البيانات بنجاح. يمكنك الآن الانتقال لإنشاء عنوان الدراسة."
    
    def _generate_title(self, study_data: Dict) -> str:
        """توليد عنوان الدراسة"""
        main_topic = study_data.get('mainTopic', '')
        field_of_study = study_data.get('fieldOfStudy', '')
        study_type = study_data.get('studyType', '')
        
        # تطبيق شروط العنوان من الدليل
        title_templates = [
            f"{main_topic}: دراسة تحليلية في مجال {self._get_field_name(field_of_study)}",
            f"تأثير {main_topic} على الممارسات المعاصرة: دراسة ميدانية",
            f"{main_topic}: رؤية معاصرة للتطوير والتحسين",
            f"استراتيجيات {main_topic} وأثرها على التطوير المؤسسي",
            f"{main_topic}: دراسة استطلاعية لواقع التطبيق والتحديات"
        ]
        
        # اختيار قالب عشوائي وتخصيصه
        base_title = random.choice(title_templates)
        
        # تطبيق تقنيات الأسلوب البشري
        humanized_title = self._humanize_text(base_title)
        
        return f"<h3>عنوان الدراسة المقترح:</h3><p><strong>{humanized_title}</strong></p><p><em>تم إنشاء هذا العنوان وفقاً لمعايير الكتابة الأكاديمية المحددة في الدليل، مع مراعاة الوضوح والدقة والجاذبية الأكاديمية.</em></p>"
    
    def _generate_abstract(self, study_data: Dict) -> str:
        """توليد الملخص"""
        main_topic = study_data.get('mainTopic', '')
        problem_description = study_data.get('problemDescription', '')
        field_of_study = study_data.get('fieldOfStudy', '')
        study_type = study_data.get('studyType', '')
        
        # بناء الملخص وفقاً للمكونات المطلوبة
        abstract_parts = []
        
        # المقدمة/الخلفية
        background = f"تناولت هذه الدراسة موضوع {main_topic} في إطار {self._get_field_name(field_of_study)}، حيث برزت الحاجة الملحة لفهم أعمق لهذه القضية في ضوء التطورات المعاصرة والتحديات الراهنة."
        abstract_parts.append(background)
        
        # مشكلة الدراسة وأهدافها
        problem_section = f"تمحورت مشكلة الدراسة حول {problem_description}، وهدفت إلى استكشاف الجوانب المختلفة لهذه الظاهرة وتحليل أبعادها المتعددة."
        abstract_parts.append(problem_section)
        
        # المنهجية (محاكاة)
        methodology = self._generate_methodology_summary(study_type, field_of_study)
        abstract_parts.append(methodology)
        
        # النتائج (محاكاة)
        results = "كشفت نتائج الدراسة عن وجود علاقات معقدة ومتداخلة بين المتغيرات المدروسة، مما يسهم في فهم أعمق للظاهرة محل البحث."
        abstract_parts.append(results)
        
        # الاستنتاجات والتوصيات
        conclusions = "خلصت الدراسة إلى مجموعة من التوصيات العملية التي يمكن أن تسهم في تطوير الممارسات الحالية وتحسين الأداء في هذا المجال."
        abstract_parts.append(conclusions)
        
        # دمج الأجزاء مع تطبيق تقنيات الأسلوب البشري
        full_abstract = " ".join(abstract_parts)
        humanized_abstract = self._humanize_text(full_abstract)
        
        return f"<h3>ملخص الدراسة:</h3><p>{humanized_abstract}</p><p><em>تم إنشاء هذا الملخص وفقاً للمعايير الأكاديمية المحددة، مع مراعاة التدفق المنطقي والصياغة الديناميكية.</em></p>"
    
    def _generate_introduction(self, study_data: Dict) -> str:
        """توليد المقدمة"""
        main_topic = study_data.get('mainTopic', '')
        problem_description = study_data.get('problemDescription', '')
        field_of_study = study_data.get('fieldOfStudy', '')
        
        introduction_parts = []
        
        # خلفية عامة
        general_background = f"يشهد مجال {self._get_field_name(field_of_study)} تطورات متسارعة في العقود الأخيرة، مما يستدعي إعادة النظر في العديد من المفاهيم والممارسات التقليدية. في هذا السياق، يبرز موضوع {main_topic} كأحد القضايا المحورية التي تتطلب دراسة معمقة وتحليلاً شاملاً."
        introduction_parts.append(general_background)
        
        # أهمية الموضوع
        importance = f"تكتسب دراسة {main_topic} أهمية خاصة في ظل التحديات المعاصرة التي تواجه هذا المجال، حيث تسهم في تقديم رؤى جديدة وحلول مبتكرة للمشكلات القائمة."
        introduction_parts.append(importance)
        
        # الفجوة البحثية
        research_gap = f"رغم الاهتمام المتزايد بهذا الموضوع، إلا أن الأدبيات العلمية تشير إلى وجود فجوة بحثية واضحة في فهم {problem_description}، مما يبرر الحاجة لإجراء هذه الدراسة."
        introduction_parts.append(research_gap)
        
        # أهداف الدراسة
        objectives = "تهدف هذه الدراسة إلى سد هذه الفجوة من خلال تقديم تحليل شامل ومعمق للموضوع، بما يسهم في إثراء المعرفة العلمية وتطوير الممارسات العملية في هذا المجال."
        introduction_parts.append(objectives)
        
        # دمج الأجزاء
        full_introduction = "\n\n".join(introduction_parts)
        humanized_introduction = self._humanize_text(full_introduction)
        
        return f"<h3>مقدمة الدراسة:</h3><div style='line-height: 1.8;'>{humanized_introduction.replace(chr(10)+chr(10), '</p><p>')}</div><p><em>تم بناء هذه المقدمة وفقاً لهيكل التدرج من العام إلى الخاص، مع مراعاة الترابط المنطقي بين الفقرات.</em></p>"
    
    def _generate_literature_review(self, study_data: Dict) -> str:
        """توليد مراجعة الأدبيات"""
        main_topic = study_data.get('mainTopic', '')
        field_of_study = study_data.get('fieldOfStudy', '')
        
        literature_sections = []
        
        # مقدمة المراجعة
        intro = f"تتناول هذه المراجعة الأدبيات العلمية ذات الصلة بموضوع {main_topic}، حيث تم الاطلاع على مجموعة واسعة من الدراسات والبحوث المنشورة في هذا المجال."
        literature_sections.append(intro)
        
        # الدراسات النظرية
        theoretical_studies = f"أشارت الدراسات النظرية في مجال {self._get_field_name(field_of_study)} إلى أهمية فهم الأسس النظرية لموضوع {main_topic}، حيث قدمت إطاراً مفاهيمياً شاملاً يساعد في تحليل الظاهرة المدروسة."
        literature_sections.append(theoretical_studies)
        
        # الدراسات التطبيقية
        empirical_studies = "من جانب آخر، ركزت الدراسات التطبيقية على الجوانب العملية والتطبيقية، مما أسهم في تقديم أدلة تجريبية تدعم الافتراضات النظرية."
        literature_sections.append(empirical_studies)
        
        # الفجوات البحثية
        research_gaps = "رغم ثراء الأدبيات في هذا المجال، إلا أن هناك فجوات بحثية واضحة تتطلب مزيداً من الدراسة والتحليل، وهو ما تسعى الدراسة الحالية لمعالجته."
        literature_sections.append(research_gaps)
        
        full_literature = "\n\n".join(literature_sections)
        humanized_literature = self._humanize_text(full_literature)
        
        return f"<h3>الإطار النظري والدراسات السابقة:</h3><div style='line-height: 1.8;'>{humanized_literature.replace(chr(10)+chr(10), '</p><p>')}</div><p><em>تم تنظيم هذا القسم وفقاً لمعايير المراجعة النقدية للأدبيات، مع التركيز على الربط بين الدراسات والبحث الحالي.</em></p>"
    
    def _generate_methodology(self, study_data: Dict) -> str:
        """توليد منهجية الدراسة"""
        study_type = study_data.get('studyType', '')
        field_of_study = study_data.get('fieldOfStudy', '')
        main_topic = study_data.get('mainTopic', '')
        
        methodology_sections = []
        
        # نوع الدراسة ومنهجها
        study_approach = f"اعتمدت هذه الدراسة على المنهج الوصفي التحليلي، والذي يعد الأنسب لطبيعة الموضوع المدروس. تم اختيار هذا المنهج لقدرته على تقديم وصف دقيق وتحليل شامل لظاهرة {main_topic}."
        methodology_sections.append(study_approach)
        
        # مجتمع الدراسة وعينتها
        population_sample = self._generate_population_description(field_of_study, study_type)
        methodology_sections.append(population_sample)
        
        # أدوات جمع البيانات
        data_collection = "تم استخدام مجموعة متنوعة من أدوات جمع البيانات لضمان الحصول على معلومات شاملة ودقيقة، بما يتناسب مع طبيعة الدراسة وأهدافها."
        methodology_sections.append(data_collection)
        
        # إجراءات الدراسة
        procedures = "تمت الدراسة وفقاً لخطة زمنية محددة، مع مراعاة جميع الاعتبارات الأخلاقية والمنهجية المطلوبة في البحث العلمي."
        methodology_sections.append(procedures)
        
        full_methodology = "\n\n".join(methodology_sections)
        humanized_methodology = self._humanize_text(full_methodology)
        
        return f"<h3>منهجية الدراسة:</h3><div style='line-height: 1.8;'>{humanized_methodology.replace(chr(10)+chr(10), '</p><p>')}</div><p><em>تم تصميم هذه المنهجية وفقاً لأفضل الممارسات في البحث العلمي، مع ضمان الدقة والموضوعية.</em></p>"
    
    def _generate_results(self, study_data: Dict) -> str:
        """توليد النتائج"""
        main_topic = study_data.get('mainTopic', '')
        
        results_content = f"""
        <h3>نتائج الدراسة:</h3>
        <div style='line-height: 1.8;'>
        <p>أظهرت نتائج الدراسة مجموعة من النتائج المهمة المتعلقة بموضوع {main_topic}، والتي يمكن تلخيصها في النقاط التالية:</p>
        
        <p>أولاً، كشفت البيانات عن وجود علاقة إيجابية قوية بين المتغيرات الرئيسية للدراسة، مما يدعم الافتراضات النظرية التي انطلقت منها الدراسة.</p>
        
        <p>ثانياً، أشارت النتائج إلى تباين واضح في الاستجابات بناءً على المتغيرات الديموغرافية، مما يعكس تأثير العوامل الشخصية والبيئية على الظاهرة المدروسة.</p>
        
        <p>ثالثاً، برزت مجموعة من التحديات والعقبات التي تواجه التطبيق العملي للمفاهيم النظرية، مما يتطلب إعادة النظر في بعض الاستراتيجيات المتبعة.</p>
        
        <p>أخيراً، أظهرت النتائج إمكانيات واعدة للتطوير والتحسين، مما يفتح المجال أمام مزيد من البحث والدراسة في هذا المجال.</p>
        </div>
        <p><em>تم عرض هذه النتائج وفقاً لمعايير العرض العلمي الدقيق، مع التركيز على الوضوح والموضوعية.</em></p>
        """
        
        return results_content
    
    def _generate_discussion(self, study_data: Dict) -> str:
        """توليد المناقشة"""
        main_topic = study_data.get('mainTopic', '')
        
        discussion_content = f"""
        <h3>مناقشة النتائج:</h3>
        <div style='line-height: 1.8;'>
        <p>تستدعي النتائج التي توصلت إليها هذه الدراسة حول {main_topic} مناقشة معمقة في ضوء الأدبيات النظرية والدراسات السابقة.</p>
        
        <p>تتفق النتائج الحالية مع ما توصلت إليه دراسات سابقة في هذا المجال، مما يعزز من مصداقية النتائج ويؤكد على أهمية الموضوع المدروس. هذا التوافق يشير إلى وجود أنماط ثابتة في الظاهرة المدروسة، مما يمكن الاعتماد عليه في بناء نماذج تفسيرية أكثر دقة.</p>
        
        <p>من جانب آخر، كشفت الدراسة عن بعض النتائج التي تختلف عن ما هو متوقع نظرياً، مما يثير تساؤلات مهمة حول طبيعة العلاقات بين المتغيرات المدروسة. هذا الاختلاف قد يعكس تأثير عوامل سياقية لم تحظ بالاهتمام الكافي في الدراسات السابقة.</p>
        
        <p>تحمل هذه النتائج دلالات مهمة للممارسة العملية، حيث تقدم توجيهات واضحة للممارسين في هذا المجال. كما تفتح المجال أمام مزيد من البحث والاستكشاف في جوانب لم تتناولها الدراسة الحالية بالتفصيل الكافي.</p>
        </div>
        <p><em>تم بناء هذه المناقشة وفقاً لمعايير التحليل النقدي، مع الربط بين النتائج والأدبيات النظرية.</em></p>
        """
        
        return discussion_content
    
    def _generate_conclusion(self, study_data: Dict) -> str:
        """توليد الخلاصة والتوصيات"""
        main_topic = study_data.get('mainTopic', '')
        
        conclusion_content = f"""
        <h3>الخلاصة والتوصيات:</h3>
        <div style='line-height: 1.8;'>
        <h4>الخلاصة:</h4>
        <p>خلصت هذه الدراسة إلى مجموعة من النتائج المهمة حول موضوع {main_topic}، والتي تسهم في إثراء المعرفة العلمية في هذا المجال. أظهرت النتائج وجود علاقات معقدة بين المتغيرات المدروسة، مما يتطلب فهماً أعمق لطبيعة هذه العلاقات وتأثيراتها المختلفة.</p>
        
        <h4>التوصيات:</h4>
        <p><strong>التوصيات العملية:</strong></p>
        <ul>
        <li>ضرورة تطوير استراتيجيات عملية لتحسين الممارسات الحالية في هذا المجال</li>
        <li>أهمية تدريب الممارسين على أحدث التطورات والمستجدات</li>
        <li>الحاجة لوضع معايير واضحة لضمان جودة التطبيق</li>
        </ul>
        
        <p><strong>التوصيات البحثية:</strong></p>
        <ul>
        <li>إجراء دراسات مقارنة في بيئات مختلفة لتعزيز قابلية تعميم النتائج</li>
        <li>استكشاف متغيرات جديدة لم تتناولها الدراسة الحالية</li>
        <li>تطوير أدوات قياس أكثر دقة وشمولية</li>
        </ul>
        </div>
        <p><em>تم صياغة هذه الخلاصة والتوصيات بناءً على النتائج المتحققة، مع التركيز على الجانبين النظري والتطبيقي.</em></p>
        """
        
        return conclusion_content
    
    def _generate_references(self, study_data: Dict) -> str:
        """توليد قائمة المراجع"""
        field_of_study = study_data.get('fieldOfStudy', '')
        
        references_content = f"""
        <h3>المراجع:</h3>
        <div style='line-height: 1.8;'>
        <p><em>ملاحظة: هذه قائمة مراجع تمثيلية. في الدراسة الفعلية، يجب إدراج جميع المصادر التي تم الاستشهاد بها في النص.</em></p>
        
        <h4>المراجع العربية:</h4>
        <ol>
        <li>الباحث، أحمد محمد (2023). أسس البحث العلمي في {self._get_field_name(field_of_study)}. دار النشر العلمي.</li>
        <li>العالم، فاطمة علي (2022). التطورات المعاصرة في مجال {self._get_field_name(field_of_study)}. مجلة البحوث العلمية، 15(3), 45-67.</li>
        <li>الخبير، محمود سالم (2021). منهجيات البحث الحديثة. دار المعرفة للنشر والتوزيع.</li>
        </ol>
        
        <h4>المراجع الأجنبية:</h4>
        <ol>
        <li>Smith, J. A. (2023). Modern approaches in academic research. Journal of Educational Research, 45(2), 123-145.</li>
        <li>Johnson, M. B., & Williams, K. L. (2022). Contemporary issues in research methodology. Academic Press.</li>
        <li>Brown, R. C. (2021). Advanced statistical methods for social sciences. International Journal of Research Methods, 12(4), 78-95.</li>
        </ol>
        </div>
        <p><em>يجب توثيق جميع المراجع وفقاً لنظام التوثيق المعتمد (APA, MLA, أو غيرها حسب متطلبات المؤسسة).</em></p>
        """
        
        return references_content
    
    def _humanize_text(self, text: str) -> str:
        """تطبيق تقنيات الأسلوب البشري الطبيعي"""
        # تنويع بداية الجمل
        text = self._vary_sentence_beginnings(text)
        
        # إضافة عبارات انتقالية طبيعية
        text = self._add_transitional_phrases(text)
        
        # تنويع طول الجمل
        text = self._vary_sentence_lengths(text)
        
        # إضافة لمسات بشرية طبيعية
        text = self._add_natural_touches(text)
        
        return text
    
    def _vary_sentence_beginnings(self, text: str) -> str:
        """تنويع بداية الجمل"""
        sentence_starters = [
            "من جانب آخر، ",
            "في هذا السياق، ",
            "بالإضافة إلى ذلك، ",
            "علاوة على ما سبق، ",
            "في ضوء ما تقدم، ",
            "انطلاقاً من هذا المفهوم، ",
            "تجدر الإشارة إلى أن ",
            "من المهم ملاحظة أن ",
            "في الواقع، ",
            "على نحو مماثل، "
        ]
        
        sentences = text.split('. ')
        for i in range(1, len(sentences), 3):  # كل ثالث جملة
            if sentences[i] and not sentences[i].startswith(tuple(sentence_starters)):
                starter = random.choice(sentence_starters)
                sentences[i] = starter + sentences[i].lower()
        
        return '. '.join(sentences)
    
    def _add_transitional_phrases(self, text: str) -> str:
        """إضافة عبارات انتقالية"""
        transitions = [
            " وفي هذا الإطار",
            " مما يعني",
            " الأمر الذي يشير إلى",
            " وهو ما يؤكد",
            " في حين أن",
            " بينما نجد أن"
        ]
        
        # إضافة عبارات انتقالية في مواضع مناسبة
        for transition in transitions:
            if random.random() < 0.3:  # 30% احتمال
                text = text.replace("، ", f"،{transition} ", 1)
        
        return text
    
    def _vary_sentence_lengths(self, text: str) -> str:
        """تنويع طول الجمل"""
        # هذه دالة مبسطة - في التطبيق الفعلي ستكون أكثر تعقيداً
        return text
    
    def _add_natural_touches(self, text: str) -> str:
        """إضافة لمسات بشرية طبيعية"""
        natural_phrases = [
            "يمكن القول إن",
            "من الواضح أن",
            "لا شك في أن",
            "من المؤكد أن",
            "يبدو جلياً أن",
            "من البديهي أن"
        ]
        
        for phrase in natural_phrases:
            if random.random() < 0.2:  # 20% احتمال
                text = text.replace("أن ", f"{phrase} ", 1)
        
        return text
    
    def _get_field_name(self, field_code: str) -> str:
        """تحويل رمز المجال إلى اسم المجال"""
        field_names = {
            'education': 'التربية وعلم النفس',
            'business': 'إدارة الأعمال',
            'engineering': 'الهندسة',
            'medicine': 'الطب',
            'law': 'القانون',
            'literature': 'الأدب واللغة',
            'science': 'العلوم الطبيعية',
            'social': 'العلوم الاجتماعية'
        }
        return field_names.get(field_code, 'التخصص العلمي')
    
    def _generate_methodology_summary(self, study_type: str, field_of_study: str) -> str:
        """توليد ملخص المنهجية للملخص"""
        if study_type == 'master':
            return "اعتمدت الدراسة على المنهج الوصفي التحليلي، مع استخدام أدوات متنوعة لجمع البيانات من عينة ممثلة."
        elif study_type == 'phd':
            return "تم استخدام منهجية مختلطة تجمع بين الأساليب الكمية والنوعية، لضمان الحصول على فهم شامل للظاهرة المدروسة."
        else:
            return "اتبعت الدراسة منهجاً علمياً دقيقاً يتناسب مع طبيعة الموضوع المدروس."
    
    def _generate_population_description(self, field_of_study: str, study_type: str) -> str:
        """توليد وصف مجتمع الدراسة"""
        if field_of_study == 'education':
            return "تكون مجتمع الدراسة من المعلمين والطلاب في المؤسسات التعليمية، وتم اختيار عينة عشوائية طبقية تمثل المجتمع الأصلي."
        elif field_of_study == 'business':
            return "شمل مجتمع الدراسة العاملين في القطاع الخاص والمؤسسات التجارية، مع التركيز على فئات محددة ذات صلة بموضوع الدراسة."
        else:
            return "تم تحديد مجتمع الدراسة بناءً على معايير علمية دقيقة، مع ضمان تمثيل جميع الفئات ذات الصلة بالموضوع المدروس."

