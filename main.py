from data_classes import DataExtractor, DataAnalisierer

if __name__ == '__main__':
    # Daten extrahieren
    extractor = DataExtractor('https://www.wetter.ch/')
    extracted_data = extractor.fetch_data()

    # Daten analysieren
    analyzer = DataAnalisierer(extracted_data)
    stats = analyzer.get_statistics()
    print(stats)
