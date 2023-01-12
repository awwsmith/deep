from pathlib import Path

import requests
import srsly
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from tqdm import tqdm

backup_dir = Path.cwd() / 'backup'

#TODO some fields contain formatting information, ex. 5.html Additional notes.
# get_text removes all tags. they can be transferred with decode_contents() https://stackoverflow.com/questions/8112922/beautifulsoup-innerhtml
class Command(BaseCommand):
    help = 'This is a test script to assess which fields and how many records have HTML formatting in them'
    
    def handle(self, *args, **options):
        items = []
        log = """"""
        for html_doc in tqdm(backup_dir.glob('*.html')):
        
            item = {}
            soup = BeautifulSoup(html_doc.read_bytes(), 'html.parser')
            try:
                item["year"] = soup.find("td", {"class": "resultsyear"}).decode_contents().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"year" + html_doc.stem
            try:
                item["author"] = soup.find("td", {"class": "authorname"}).decode_contents().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"author" + html_doc.stem
            # still need to parse display to get author ids, there's also author_display?
            try:
                item["title"] = soup.find("td", {"class": "playname"}).decode_contents().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"title" + html_doc.stem
        
            # Reference Information
            try:
                item['deep_id'] = html_doc.stem
            except Exception as e:
                log += "[*]"+"deep_id" + html_doc.stem
            try:
                item["deep_id_display"] = soup.find('span', text = 'DEEP #:').parent.decode_contents().replace('DEEP #:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"deep_id_display" + html_doc.stem
            try:
                item["greg_full"] = soup.find('span', text = 'Greg #:').parent.decode_contents().replace('Greg #:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"greg_full" + html_doc.stem
                item["greg_full"] = ""
            try:
                item["stc"] = soup.find('span', text = 'STC/Wing #:').parent.decode_contents().replace('STC/Wing #:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"stc" + html_doc.stem
                item["stc"] = ""
            try:
                item["record_type"] = soup.find('span', text = 'Record Type:').parent.decode_contents().replace('Record Type:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"record_type" + html_doc.stem
                item["record_type"] = ""
            try:
                item['play_type'] = soup.find('span', text = 'Play Type:').parent.decode_contents().replace('Play Type:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"play_type" + html_doc.stem
                item['play_type'] = ""
            try:
                item["genre"] = soup.find('span', text = 'Genre (Annals):').parent.decode_contents().replace('Genre (Annals):','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"genre" + html_doc.stem
                item["genre"] = ""
            try:
                item["book_edition"] = soup.find('span', text = 'Book Edition:').parent.decode_contents().replace('Book Edition:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"book_edition" + html_doc.stem
                item["book_edition"] = ""
            try:
                item["play_edition"] = soup.find('span', text = 'Play Edition:').parent.decode_contents().replace('Play Edition:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"play_edition" + html_doc.stem
                item["play_edition"] = ""
            try:
                item["format"] = soup.find('span', text = 'Format:').parent.decode_contents().replace('Format:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"format" + html_doc.stem
                item["format"] = ""
            try:
                item["leaves"] = soup.find('span', text = 'Leaves:').parent.decode_contents().replace('Leaves:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"leaves" + html_doc.stem
                item["leaves"] = ""
            try:
                item["blackletter"] = soup.find('span', text = 'Black Letter:').parent.decode_contents().replace('Black Letter:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"blackletter" + html_doc.stem
                item["blackletter"] = ""
            try:
                item["date_first_publication_display"] = soup.find('span', text = 'Date of First Publication:').parent.decode_contents().replace('Date of First Publication:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"genre" + html_doc.stem
                item["date_first_publication_display"] = ""
            try:
                item["date_first_performance"] = soup.find('span', text = 'Date of First Production:').parent.decode_contents().replace('Date of First Production:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"date_first_performance" + html_doc.stem
                item["date_first_performance"] = ""
            try:
                item["company_first_performance"] = soup.find('span', text = 'Company of First Production:').parent.decode_contents().replace('Company of First Production:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"company_first_performance" + html_doc.stem
                item["company_first_performance"] =""
            try:
                item["company_attribution"]= soup.find('span', text = 'Company Attribution:').parent.decode_contents().replace('Company Attribution:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"company_attribution" + html_doc.stem
                item["company_attribution"] =""
            try:
                item["total_editions"]= soup.find('span', text = 'Total Editions:').parent.decode_contents().replace('Total Editions:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"total_editions" + html_doc.stem
                item["total_editions"] = ""
            
            try:
                item["in_collection"] = soup.find('span', text = 'In Collection:').parent.decode_contents().replace('In Collection:','').strip().encode('ISO-8859-1').decode('utf-8')
                link = soup.find('span', text = 'In Collection:').parent.find('a')
                item["in_collection_link_text"] = link.decode_contents().encode('ISO-8859-1').decode('utf-8')
                item["in_collection_link_href"] = link['href'].replace("javascript:showRecord('",'').replace("')", '')
            except Exception as e:
                log += "[*]"+"in_collection" + html_doc.stem
                item["in_collection"] = ""
                item["in_collection_link_text"] = ""
                item["in_collection_link_href"] = ""
            #TODO handle list of links in Django
            try:
                item["collection_contains"] = soup.find('span', text = 'Collection contains:').parent.decode_contents().replace('Collection contains:','').strip().encode('ISO-8859-1').decode('utf-8')
                item["collection_contains_links"] = []
                links = soup.find('span', text = 'Collection contains:').parent.find_all('a')
                for link in links:
                    text = link.decode_contents().encode('ISO-8859-1').decode('utf-8') 
                    href = link['href'].replace("javascript:showRecord('",'').replace("')", '')
                    item["collection_contains_links"].append(dict(text=text, href=href))
            except Exception as e:
                log += "[*]"+"collection_contains" + html_doc.stem
                item["collection_contains"] = ""
                item["collection_contains_links"] = []
            try:
                item["variants"] = soup.find('span', text = 'Variants:').parent.decode_contents().replace('Variants:','').strip().encode('ISO-8859-1').decode('utf-8')
                links = soup.find('span', text = 'Variants:').parent.find_all('a')
                item["variant_links"] = []
                for link in links:
                    text = link.decode_contents().encode('ISO-8859-1').decode('utf-8') 
                    href = link['href'].replace("javascript:showRecord('",'').replace("')", '')
                    item["variant_links"].append(dict(text=text, href=href))

            except Exception as e:
                log += "[*]"+"variants" + html_doc.stem
                item["variants"]  = ""
                item["variant_links"] = []
            try:
                item["independent_playbook"] = soup.find('span', text = 'Also appears as a bibliographically independent playbook in').parent.decode_contents().replace('Also appears as a bibliographically independent playbook in','').strip().encode('ISO-8859-1').decode('utf-8')
                link  = soup.find('span', text = 'Also appears as a bibliographically independent playbook in').parent.find('a')
                item["independent_playbook_link_text"] = link.decode_contents().encode('ISO-8859-1').decode('utf-8')
                item["independent_playbook_link_href"] = link['href'].replace("javascript:showRecord('",'').replace("')", '')
            except Exception as e:
                log += "[*]"+"independent_playbook" + html_doc.stem
                item["independent_playbook"] = ""
                item["independent_playbook_link_text"] = ""
                item["independent_playbook_link_href"] = ""
            
            try:
                item["also_in_collection"] = soup.find('span', text = 'Also appears in collection:').parent.decode_contents().replace('Also appears in collection:','').strip().encode('ISO-8859-1').decode('utf-8')
                link  = soup.find('span', text = 'Also appears in collection:').parent.find('a')
                item["also_in_collection_link_text"] = link.decode_contents().encode('ISO-8859-1').decode('utf-8')
                item["also_in_collection_link_href"] = link['href'].replace("javascript:showRecord('",'').replace("')", '')
            except Exception as e:
                log += "[*]"+"also_in_collection" + html_doc.stem
                item["also_in_collection"] =""
                item["also_in_collection_link_text"] = ""
                item["also_in_collection_link_href"] = ""
            
            #Title-Page Features
            try:
                item["title_page_title"] = soup.find('span', text = 'Title:').parent.decode_contents().replace('Title:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"title_page_title" + html_doc.stem
                item["title_page_title"] =""
            try:
                item["title_page_author"] = soup.find('span', text = 'Author:').parent.decode_contents().replace('Author:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"title_page_author" + html_doc.stem
                item["title_page_author"] = ""
            try:
                item["title_page_performance"] = soup.find('span', text = 'Performance:').parent.decode_contents().replace('Performance:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"title_page_performance" + html_doc.stem
                item["title_page_performance"] = ""
            try:
                item["title_page_imprint"] = soup.find('span', text = 'Imprint:').parent.decode_contents().replace('Imprint:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"title_page_imprint" + html_doc.stem
                item["title_page_imprint"] = ""

            try:
                item["title_page_latin_motto"] = soup.find('span', text = 'Latin Motto:').parent.decode_contents().replace('Latin Motto:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"title_page_latin_motto" + html_doc.stem
                item["title_page_latin_motto"] = ""

            try:
                item["title_page_illustration"] = soup.find('span', text = 'Illustration:').parent.decode_contents().replace('Illustration:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"title_page_illustration" + html_doc.stem
                item["title_page_illustration"] = ""
            
            
            #Paratextual Material
            try:
                item["paratext_dedication"] = soup.find('span', text = 'Dedication:').parent.decode_contents().replace('Dedication:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"paratext_dedication" + html_doc.stem
                item["paratext_dedication"] = ""
            try:
                item["paratext_commendatory_verses"] = soup.find('span', text = 'Commendatory Verses:').parent.decode_contents().replace('Commendatory Verses:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"paratext_commendatory_verses" + html_doc.stem
                item["paratext_commendatory_verses"] = ""
                
            
            try:
                item["paratext_to_the_reader"] = soup.find('span', text = 'To the Reader:').parent.decode_contents().replace('To the Reader:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"paratext_to_the_reader" + html_doc.stem
                item["paratext_to_the_reader"]= ""
            try:
                item["paratext_charachter_list"] = soup.find('span', text = 'Character List:').parent.decode_contents().replace('Character List:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"paratext_charachter_list" + html_doc.stem
                item["paratext_charachter_list"] = ""
            try:
                item["paratext_errata"] = soup.find('span', text = 'Errata:').parent.decode_contents().replace('Errata:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"paratext_errata" + html_doc.stem
                item["paratext_errata"] = ""
            try:
                item["paratext_actor_list"] = soup.find('span', text = 'Actor List:').parent.decode_contents().replace('Actor List:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"paratext_actor_list" + html_doc.stem
                item["paratext_actor_list"]= ""
            try:
                item["paratext_other_paratexts"] = soup.find('span', text = 'Other Paratexts:').parent.decode_contents().replace('Other Paratexts:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"paratext_other_paratexts" + html_doc.stem
                item["paratext_other_paratexts"] = ""
            try:
                item["paratext_argument"] = soup.find('span', text = 'Argument:').parent.decode_contents().replace('Argument:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"paratext_argument" + html_doc.stem
                item["paratext_argument"] = ""
            # TODO was in title page, not para
            try:
                item["paratext_explicit"] = soup.find('span', text = 'Explicit:').parent.decode_contents().replace('Explicit:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"paratext_explicit" + html_doc.stem
                item["paratext_explicit"] = ""
            
            #Stationer Information
            try:
                item["stationer_printer"] = soup.find('span', text = 'Printer:').parent.decode_contents().replace('Printer:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"stationer_printer" + html_doc.stem
                item["stationer_printer"] = ""
            try:
                item["stationer_imprint_location"] = soup.find('span', text = 'Imprint Location:').parent.decode_contents().replace('Imprint Location:','').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"stationer_imprint_location" + html_doc.stem
                item["stationer_imprint_location"] = ""
            try:
                item["stationer_entries_in_register"] = soup.find('span', text = "Entries in Stationers' Register:").parent.decode_contents().replace("Entries in Stationers' Register:",'').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"stationer_entries_in_register" + html_doc.stem
                item["stationer_entries_in_register"] = ""
            try:
                item["stationer_additional_notes"] = soup.find('span', text = "Additional Notes:").parent.decode_contents().replace("Additional Notes:",'').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"stationer_additional_notes" + html_doc.stem
                item["stationer_additional_notes"] = ""
            try:
                item["stationer_publisher"] = soup.find('span', text = "Publisher:").parent.decode_contents().replace("Publisher:",'').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"stationer_publisher" + html_doc.stem
                item["stationer_publisher"] = ""
            try:
                item["stationer_bookseller"] = soup.find('span', text = "Bookseller:").parent.decode_contents().replace("Bookseller:",'').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"stationer_bookseller" + html_doc.stem
                item["stationer_bookseller"] = ""
            try:
                item["stationer_publisher"] = soup.find('span', text = "Publisher:").parent.decode_contents().replace("Publisher:",'').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"stationer_publisher" + html_doc.stem
                item["stationer_publisher"] = ""
            try:
                item["stationer_colophon"] = soup.find('span', text = "Colophon:").parent.decode_contents().replace("Colophon:",'').strip().encode('ISO-8859-1').decode('utf-8')
            except Exception as e:
                log += "[*]"+"stationer_colophon" + html_doc.stem
                item["stationer_colophon"] = ""
            
            items.append(item)
        srsly.write_jsonl('test_web_item_data.jsonl', items)
        print(len(items))