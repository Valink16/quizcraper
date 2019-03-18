def get_terms(web_driver, quiz_url, start = 0, end = -1):
    """
        returns a list of terms which go from number<start> to number<end>
    """
    web_driver.get(quiz_url)
    terms = web_driver.find_elements_by_xpath("//span[starts-with(@class,'TermText')]")
    print("Found {} non-translated terms...".format(len(terms)))
    for term in terms:
        print(term.text)