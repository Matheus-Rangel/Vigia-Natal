from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

import os
import json

driver = webdriver.Chrome('G:\Meu Drive\Codes\Python\Selenium\drivers\chromedriver.exe')
logging.basicConfig(level=logging.ERROR, filename='bot_despesa_natal.log')

def salvar_json(despesas):
    try:
        instituicao = despesas[0]['instituicao']
        orgao = despesas[0]['orgao']
        root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Despesas')
        instituicaoPath = os.path.join(root, instituicao)
        orgaoPath = os.path.join(instituicaoPath, orgao + ".json")
        if not os.path.exists(root):
            os.makedirs(root)
        if not os.path.exists(instituicaoPath):
            os.makedirs(instituicaoPath)
        f= open(orgaoPath,"wb+")
        dados = json.dumps(obj = despesas, indent = 1, ensure_ascii = False).encode('utf-8')
        print(dados)
        f.write(dados)
    except:
        logging.exception("Salva Json, Instituição:{}, Orgao:{}".format(instituicao, orgao))

def getIds():
    time.sleep(1)
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#list .ui-widget-content")))
    itens = driver.find_elements_by_css_selector('#list .ui-widget-content')
    ids = []
    for i in itens:
        ids.append(i.get_attribute('id'))
    return ids


def getInstituicoes():
    try:
        ids = getIds()
        for id in ids:
            selector = '[id="' + id + '"] td'
            print(selector)
            try:
                WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                dado = driver.find_element_by_css_selector(selector)
                dado.click()
                getOrgaos()
            except:
                logging.exception("GetInstituicao, ID: {}".format(id))
                continue
    finally:
        driver.quit()

def getOrgaos():
    try:
        ids = getIds()
        for id in ids:
            selector = '[id="' + id + '"] td'
            print(selector)
            try:
                WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                dado = driver.find_element_by_css_selector(selector)
                dado.click()
                getElementos()
            except:
                logging.exception("GetOrgaos, ID: {}".format(id))
                continue
    finally:
        element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Instituições')]")))
        element.click()
        time.sleep(1)
        WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#list .ui-widget-content")))

def getElementos():
    try:
        despesas = []
        ids = getIds()
        for id in ids:
            selector = '[id="' + id + '"] td'
            try:
                WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                dado = driver.find_element_by_css_selector(selector)
                dado.click()
                despesas += getCredores()
            except:
                logging.exception("GetElementos, ID: {}".format(id))
                continue
    finally:
        element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Orgãos')]")))
        element.click()
        time.sleep(1)
        WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#list .ui-widget-content")))
        salvar_json(despesas)

def getCredores():
    try:
        despesas = []
        ids = getIds()
        for id in ids:
            selector = '[id="' + id + '"] td'
            try:
                WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                dado = driver.find_element_by_css_selector(selector)
                dado.click()
                despesas += getEmpenhos()
            except:
                logging.exception("GetCredores, ID: {}".format(id))
                continue
    finally:
        element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Elementos')]")))
        element.click()
        time.sleep(1)
        WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#list .ui-widget-content")))
        return despesas

def getEmpenhos():
    try:
        despesas = []
        ids = getIds()
        for id in ids:
            selector = '[id="' + id + '"] td'
            try:
                WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                dado = driver.find_element_by_css_selector(selector)
                dado.click()
                despesas.append(getDespesa())
            except:
                logging.exception("GetEmpenhos, ID: {}".format(id))
                continue
    finally:
        element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Credores')]")))
        element.click()
        time.sleep(1)
        WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#list .ui-widget-content")))
        return despesas

def getDespesa():
    time.sleep(1)
    element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#list [title=\"EMPENHO\"]")))
    element.click()
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".dados_empenhos")))
    despesa = getInformation()
    element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Empenhos')]")))
    element.click()
    time.sleep(1)
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#list .ui-widget-content")))
    return despesa

def getInformation():
    elementos = driver.find_elements_by_css_selector('.historico_valores tr td')
    despesa = {"instituicao":elementos[0].text, "orgao":elementos[5].text, "credor":elementos[15].text, "empenhado":elementos[21].text,
                "anulado":elementos[22].text, "liquidado":elementos[23].text, "pago":elementos[22].text}

    elementos = driver.find_elements_by_css_selector('.dados_empenhos tr td')
    despesa['data'] = elementos[9].text
    despesa['historico'] = elementos[13].text

    itens = []
    elementos = driver.find_elements_by_css_selector('#list_itens tr td')
    for i in range(4,len(elementos),4):
        item = {'descricao':elementos[i].text, 'quantidade':elementos[i + 1].text, 'valor_unitario':elementos[i + 2].text, 'valor_total':elementos[i + 3].text}
        itens.append(item)
    despesa['itens'] = itens
    return despesa

if __name__ == '__main__':
    driver.get('https://www.natal.rn.gov.br/transparencia/despesas#')
    elem = driver.find_element_by_link_text('Despesas por Instituição / Orgão')
    elem.click()
    getInstituicoes()
