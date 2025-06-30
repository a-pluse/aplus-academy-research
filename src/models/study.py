from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class Study(db.Model):
    __tablename__ = 'studies'
    
    id = db.Column(db.Integer, primary_key=True)
    study_type = db.Column(db.String(50), nullable=False)  # master, phd, research
    field_of_study = db.Column(db.String(100), nullable=False)
    main_topic = db.Column(db.Text, nullable=False)
    problem_description = db.Column(db.Text, nullable=False)
    keywords = db.Column(db.Text)
    
    # Generated content for each section
    title_content = db.Column(db.Text)
    abstract_content = db.Column(db.Text)
    introduction_content = db.Column(db.Text)
    literature_content = db.Column(db.Text)
    methodology_content = db.Column(db.Text)
    results_content = db.Column(db.Text)
    discussion_content = db.Column(db.Text)
    conclusion_content = db.Column(db.Text)
    references_content = db.Column(db.Text)
    
    # Additional inputs for each section
    additional_inputs = db.Column(db.Text)  # JSON string
    
    # Metadata
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    completed_sections = db.Column(db.Text)  # JSON array of completed section names
    
    def __init__(self, **kwargs):
        super(Study, self).__init__(**kwargs)
        self.additional_inputs = json.dumps({})
        self.completed_sections = json.dumps([])
    
    def get_additional_inputs(self):
        try:
            return json.loads(self.additional_inputs or '{}')
        except:
            return {}
    
    def set_additional_inputs(self, inputs):
        self.additional_inputs = json.dumps(inputs)
    
    def get_completed_sections(self):
        try:
            return json.loads(self.completed_sections or '[]')
        except:
            return []
    
    def set_completed_sections(self, sections):
        self.completed_sections = json.dumps(sections)
    
    def add_completed_section(self, section):
        sections = self.get_completed_sections()
        if section not in sections:
            sections.append(section)
            self.set_completed_sections(sections)
    
    def to_dict(self):
        return {
            'id': self.id,
            'study_type': self.study_type,
            'field_of_study': self.field_of_study,
            'main_topic': self.main_topic,
            'problem_description': self.problem_description,
            'keywords': self.keywords,
            'title_content': self.title_content,
            'abstract_content': self.abstract_content,
            'introduction_content': self.introduction_content,
            'literature_content': self.literature_content,
            'methodology_content': self.methodology_content,
            'results_content': self.results_content,
            'discussion_content': self.discussion_content,
            'conclusion_content': self.conclusion_content,
            'references_content': self.references_content,
            'additional_inputs': self.get_additional_inputs(),
            'completed_sections': self.get_completed_sections(),
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

