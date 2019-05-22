# -*- coding: utf-8 -*-

import logging

def get_terms(web_driver, quiz_url, start = 0, end = -1):
    """
        returns a list tuples of terms which go from number<start> to number<end>
    """
    term_class_name = "SetPageTerms-term" # Class name of "terms"
    # xpaths relative to the webelements with the <term_class_name> class
    first_term_relative_xpath = "div/div/div[1]/div/div[1]/div/a/span"
    second_term_relative_xpath = "div/div/div[1]/div/div[2]/div/a/span"
    web_driver.get(quiz_url)

    terms = web_driver.find_elements_by_class_name(term_class_name)
    logging.info("Found {} terms".format(len(terms)))
    if end == -1:
        end = len(terms) - 1
    
    return [(t.find_element_by_xpath(first_term_relative_xpath).text, t.find_element_by_xpath(second_term_relative_xpath).text) for t in terms[start:end]]