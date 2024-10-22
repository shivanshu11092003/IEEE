import scrapy
import requests
from transformers import pipeline  # Add this line to import the pipeline


class CyberIncidentSpider(scrapy.Spider):
    name = 'cyber_incident'
    start_urls  = [
    'https://us-cert.cisa.gov/ncas',
    'https://nvd.nist.gov/',
    'https://infosecwriteups.com/',
    'https://thehill.com/policy/cybersecurity',
    'https://techrepublic.com/article/what-is-cybersecurity-and-why-is-it-important/',
    'https://www.theinformation.com/articles',
    'https://thehackernews.com/search/label/Cyber%20Attack',
    'https://timesofindia.indiatimes.com/topic/cybersecurity',
    'https://economictimes.indiatimes.com/news/cybersecurity',
    'https://www.hindustantimes.com/',
    'https://www.bbc.com/news/technology',
    'https://www.cnn.com/business/tech',
    'https://www.forbes.com/cybersecurity/',
    'https://www.zdnet.com/topic/security/',
    'https://www.cnet.com/topics/security/',
    'https://www.securityweek.com/',
    'https://www.darkreading.com/',
    'https://www.infosecurity-magazine.com/',
    'https://www.cybersecurityinsiders.com/',
    'https://krebsonsecurity.com/',
    'https://threatpost.com/',
    'https://www.scmagazine.com/',
    'https://techcrunch.com/tag/cybersecurity/',
    'https://www.wired.com/category/security/',
    'https://www.bloomberg.com/technology',
    'https://www.reuters.com/technology',
    'https://www.govinfosecurity.com/',
    'https://www.csoonline.com/',
    'https://us-cert.cisa.gov/',
    'https://securityaffairs.co/',
    'https://blog.malwarebytes.com/',
    'https://www.paloaltonetworks.com/blog',
    'https://fortiguard.com/',
    'https://www.fireeye.com/blog.html',
    'https://www.symantec.com/blogs/',
    'https://www.bitdefender.com/blogs/',
    'https://www.securityintelligence.com/',
    'https://cloudsecurityalliance.org/',
    'https://arstechnica.com/information-technology/',
    'https://venturebeat.com/security/',
    'https://www.techradar.com/news/security',
    'https://www.hackerone.com/blog',
    'https://privacynews.com/',
    'https://threathunting.net/',
    'https://www.theregister.com/security/',
    'https://securosis.com/',
    'https://www.beyondtrust.com/blog',
    'https://www.trendmicro.com/en_us/research.html',
    'https://cybereason.com/blog/',
    'https://varonis.com/blog/',
    'https://www.knowbe4.com/blog',
    'https://www.cyberark.com/resources/blog/',
    'https://blog.checkpoint.com/',
    'https://www.dell.com/en-us/security',
    'https://www.troyhunt.com/',
    'https://www.f-secure.com/weblog',
    'https://www.sophos.com/en-us/blogs',
    'https://dzone.com/security',
    'https://cylance.com/blog/',
    'https://crowdstrike.com/blog/',
    'https://resilience.com/blog/',
    'https://blog.avast.com/cybersecurity',
    'https://netmagazine.com/news/security',
    'https://infosec-journal.com/',
    'https://www.sciencedirect.com/topics/computer-science/cyber-security',
    'https://informationweek.com/security',
    'https://www.helpnetsecurity.com/',
    'https://darknetdiaries.com/',
    'https://cyberdefensemagazine.com/',
    'https://threathunter.com/',
    'https://kaspersky.com/resource-center/threats',
    'https://www.cybersecurity360.com/',
    'https://privacytools.io/',
    'https://cybernews.com/',
    'https://nakedsecurity.sophos.com/',
    'https://avira.com/en/learn/security',
    'https://checkmarx.com/blog',
    'https://nssgroupe.com/blog',
    'https://www.sans.org/blogs',
    'https://securityaffairs.com/',
    'https://cyber-scoop.com/',
    'https://securitylab.ru/en/',
    'https://www.bmc.com/blogs/security',
    'https://onionsearchengine.com/blog/cybersecurity',
    'https://pivotal.io/blog/security',
    'https://www.net-security.org/',
    'https://khanacademy.org/computing/computer-science/internet-intro/internet-security/v/introduction-to-internet-security',
    'https://www.businessinsider.com/cybersecurity',

        ]
    

    allowed_domains= [
    'us-cert.cisa.gov/ncas',
    'nvd.nist.gov/',
    'infosecwriteups.com',
    'thehill.com/policy/cybersecurity',
    'techrepublic.com/article/what-is-cybersecurity-and-why-is-it-important/',
    'theinformation.com/articles',
    'thehackernews.com',
    'timesofindia.indiatimes.com',
    'economictimes.indiatimes.com',
    'hindustantimes.com',
    'bbc.com',
    'cnn.com',
    'forbes.com',
    'zdnet.com',
    'cnet.com',
    'securityweek.com',
    'darkreading.com',
    'infosecurity-magazine.com',
    'cybersecurityinsiders.com',
    'krebsonsecurity.com',
    'threatpost.com',
    'scmagazine.com',
    'techcrunch.com',
    'wired.com',
    'bloomberg.com',
    'reuters.com',
    'govinfosecurity.com',
    'csoonline.com',
    'us-cert.cisa.gov',
    'securityaffairs.co',
    'malwarebytes.com/blog',
    'paloaltonetworks.com/blog',
    'fortiguard.com',
    'fireeye.com/blog',
    'symantec.com/blogs',
    'bitdefender.com/blogs',
    'securityintelligence.com',
    'cloudsecurityalliance.org',
    'arstechnica.com',
    'venturebeat.com',
    'techradar.com',
    'hackerone.com/blog',
    'privacynews.com',
    'threathunting.net',
    'theregister.com',
    'securosis.com',
    'beyondtrust.com/blog',
    'trendmicro.com/en_us/research.html',
    'cybereason.com/blog',
    'varonis.com/blog',
    'knowbe4.com/blog',
    'cyberark.com/resources/blog',
    'checkpoint.com/blogs',
    'dell.com/en-us/security',
    'troyhunt.com',
    'f-secure.com/weblog',
    'sophos.com/en-us/blogs',
    'dzone.com/security',
    'cylance.com/blog',
    'crowdstrike.com/blog',
    'resilience.com/blog',
    'avast.com/cybersecurity-blog',
    'netmagazine.com/news/security',
    'infosec-journal.com',
    'sciencedirect.com/topics/computer-science/cyber-security',
    'informationweek.com/security',
    'helpnetsecurity.com',
    'darknetdiaries.com',
    'cyberdefensemagazine.com',
    'threathunter.com',
    'kaspersky.com/resource-center/threats',
    'cybersecurity360.com',
    'privacytools.io',
    'cybernews.com',
    'nakedsecurity.sophos.com',
    'avira.com/en/learn/security',
    'checkmarx.com/blog',
    'nssgroupe.com/blog',
    'sans.org/blogs',
    'securityaffairs.com',
    'cyber-scoop.com',
    'securitylab.ru/en/',
    'bmc.com/blogs/security',
    'onionsearchengine.com/blog/cybersecurity',
    'pivotal.io/blog/security',
    'net-security.org',
    'khanacademy.org/computing/computer-science/internet-intro/internet-security/v/introduction-to-internet-security',
    'businessinsider.com/cybersecurity',
    ]


    keywords = [
        'cyber attack', 'security updates', 'data breach', 'ransomware', 'phishing',
        'malware', 'DDoS', 'zero-day vulnerability', 'cyber threat', 'firewall breach',
        'SQL injection', 'social engineering', 'encryption', 'password leak', 'hacker',
        'identity theft', 'spyware', 'APT (Advanced Persistent Threat)', 'botnet',
        'vulnerability', 'cybercrime', 'cyber espionage', 'rootkit', 'insider threat',
        'cross-site scripting', 'cyber resilience', 'cryptojacking', 'cybersecurity law',
        'penetration testing', 'cyber warfare', 'bug bounty', 'backdoor', 'two-factor authentication',
        'patch management', 'zero trust', 'cloud security', 'IoT security', 'incident response',
        'supply chain attack', 'keylogger', 'breach notification', 'threat intelligence',
        'cyber policy', 'vulnerability assessment', 'data exfiltration', 'cyber insurance',
        'phishing scam', 'trojan horse', 'digital forensics', 'dark web', 'SIEM (Security Information and Event Management)'
    ]

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def parse(self, response):
        for article in response.css('a[href]::attr(href)').getall():
            if article.startswith(('http://', 'https://')):
                yield response.follow(article, self.parse_article)

        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        title = response.css('h1::text').get()
        link = response.url
        date = response.css('.publish-date::text').get()
        content = ' '.join(response.css('p::text').getall())

        if self.is_cybersecurity_related(content):
            summary = self.summarize_content(content)
            matching_keywords = self.get_matching_keywords(content)

            yield {
                'title': title,
                'link': link,
                'date': date,
                'summary': summary,
                'category': matching_keywords,
            }

            url = 'https://10.21.97.82:8888/NeuraSecure/data_insert/' 
            data = {
                'title': title,
                'link': link,
                'content': content,
                'summary': summary,
                'category': matching_keywords,
            }

            response = requests.post(url, json=data)

            if response.status_code == 201:  
                print('Post created successfully:', response.json())
            else:
                print('Failed to create post:', response.status_code, response.text)

    def summarize_content(self, content):
        # Summarize the content using Hugging Face
        if len(content.split()) > 50:  # Summarize only if content length is sufficient
            summary = self.summarizer(content, max_length=130, min_length=30, do_sample=False)
            return summary[0]['summary_text']
        return content  # Return the original content if too short

    def get_matching_keywords(self, content):
        """Get keywords that match the content."""
        return [keyword for keyword in self.keywords if keyword in content.lower()]

    def is_cybersecurity_related(self, content):
        return len(self.get_matching_keywords(content)) >= 2