from crawler import Crawler

if __name__ == "__main__":
    base_url = "https://sport050.nl/sporten-in-groningen/"
    crawler = Crawler(base_url)
    num_iterations = 5
    
    for data in zip(range(num_iterations), crawler):
        print(data)