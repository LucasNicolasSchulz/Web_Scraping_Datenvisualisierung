from data_classes import DataExtractor, DataAnalyzer

if __name__ == '__main__':
    extractor = DataExtractor('https://www.wetter.ch/')
    weather_data = extractor.fetch_data()

    analyzer = DataAnalyzer(weather_data)
    analyzer.analyze_data()
    analyzer.visualize_data()
