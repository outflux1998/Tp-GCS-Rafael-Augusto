import os

from YAML_parser import YAMLParser
from feature_engineering_parser import FeatureEngineeringParser
from model_parser import ModelParser

# Verifica se o script está sendo executado como programa principal
if __name__ != "__main__":
    exit()

def get_config():
    """
    Função principal para ler e analisar arquivos de configuração.

    Esta função itera pelos arquivos YAML no diretório 'yamls',
    analisa a configuração, realiza engenharia de features e extrai
    configurações do modelo.

    :return: None
    """
    # Inicializa os parsers
    initialParser = YAMLParser
    featureEngineringParser = FeatureEngineeringParser
    modelParser = ModelParser

    # Itera pelos arquivos YAML no diretório 'yamls'
    for file in os.listdir('yamls'):
        filepath = os.path.join('yamls', file)

        # Analisa a configuração YAML inicial
        config = initialParser(filepath).parse()

        # Analisa as configurações de engenharia de features
        features_configs, columns_set_alias = featureEngineringParser(filepath).parse(config['feature_engineering'])
        del config['feature_engineering']

        # Analisa as configurações do modelo
        model_configs = modelParser(columns_set_alias).parse(config['model'])
        del config['model']

        # Exibe as configurações analisadas
        print("FEATURES")
        print(features_configs)
        print(3 * '\n')
        print(20 * '-')
        print(3 * '\n')
        print(model_configs)

get_config()
