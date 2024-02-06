from crawler_data_reader import read_crawler_data
from index_builder import build_index, build_index_with_stemming, build_positional_index, build_content_index
from statistics_generator import generate_statistics
from file_writer import write_to_file

def main():
    filepath = 'crawled_urls.json'  
    docs = read_crawler_data(filepath)

    non_positional_index = build_index(docs)
    write_to_file('title.non_pos_index.json', non_positional_index)

    stemmed_index = build_index_with_stemming(docs)
    write_to_file('mon_stemmer.title.non_pos_index.json', stemmed_index)

    positional_index = build_positional_index(docs)
    write_to_file('title.pos_index.json', positional_index)

    content_index = build_content_index(docs)
    write_to_file('content.non_pos_index.json', content_index)

    stats = generate_statistics(docs)
    write_to_file('metadata.json', stats)

if __name__ == '__main__':
    main()
