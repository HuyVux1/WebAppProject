import scrapy
page = 2
class WebImagesSpider(scrapy.Spider):
    name = "xray_image"
    start_urls = ["https://www.shutterstock.com/search/healthy+lungs+xray"]
    def parse(self, response):
        global page
        for image in response.css("div.z_h_b900b"):
            if (image.css("a.z_h_81637 img::attr(src)").get() is not None):
                 yield {
                "link": image.css("a.z_h_81637 img::attr(src)").get(),
                "title": image.css("a.z_h_81637 img::attr(alt)").get(),
        }
        next_page = f"https://www.shutterstock.com/search/healthy+lungs+xray?page={page}" 
        page += 1
        if page <= 10:
            yield response.follow(next_page, callback=self.parse)
