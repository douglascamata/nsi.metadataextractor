#coding: utf-8
import sys
from os import listdir
from os.path import abspath, dirname, join

import unittest
from should_dsl import should, should_not
from nsi.metadataextractor.xml_parser import Parser
from nsi.metadataextractor.extractor import Preparator, TccExtractor

ROOT_PATH = abspath(dirname(__file__))
TEMPLATES_PATH = join(ROOT_PATH, '..', 'templates')

class TestPreparation(unittest.TestCase):

	def setUp(self):
		self.parse = Parser(join(TEMPLATES_PATH, 'tcc.xml'))
		self.tipo = 'obtencaograu'
		self.nome = '1'
		self.preparator = Preparator(self.tipo, self.nome)
		
	def test_pdf_document_exists(self):
		self.obtencaograu_pdf_document = self.nome + '.pdf'
		self.obtencaograu_pdf_documents = listdir(join(ROOT_PATH, '..', 'articles', 'obtencaograu'))
		self.obtencaograu_pdf_document |should| be_into (self.obtencaograu_pdf_documents)
	
	def test_obtencao_grau_document_pdf_to_txt_convertion(self):
		self.converted_document = self.nome + '.txt'
		one_page_hash = self.parse.onepage_metadata
		page = one_page_hash['page']
		self.preparator.convert_document(page, page)
		self.obtecaograu_converted_documents = listdir(join(ROOT_PATH, '..', 'articles', 'obtencaograu', 'converted'))
		self.converted_document |should| be_into (self.obtecaograu_converted_documents)

	def test_text_should_be_a_list(self):
		self.doc = self.preparator.open_document()
		type(self.doc) |should| equal_to (list)

class TestTccExtractor(unittest.TestCase):

	def setUp(self):
		self.extractor = TccExtractor('1')

	def test_author_type_metadata_has_to_exist(self):
		self.extractor.author_metadata |should| equal_to( 
			["DALINE GONÇALVES MORAES DE SOUZA",
			"KAROLYNE ALMEIDA SIQUEIRA",
			"RAFAEL LEITE DE FREITAS"])

 
if __name__ == '__main__':
	unittest.main()

	

		
		