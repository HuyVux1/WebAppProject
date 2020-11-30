import scrapy

class WebImagesSpider(scrapy.Spider):
    name = "xray_image"
    start_urls = ["https://www.shutterstock.com/search/healthy+lungs+xray"]

    def parse(self, response):
        for image in response.css("div.z_h_b900b"):
            yield {
                "link": image.css("a.z_h_81637 img::attr(src)").get(),
                "title": image.css("a.z_h_81637 img::attr(alt)").get(),
            }