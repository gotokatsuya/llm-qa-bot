from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator

if __name__ == "__main__":
    print(
        VectorstoreIndexCreator().
        from_loaders([CSVLoader(file_path="faq.csv")]).
        query("どの端末から入力できますか？それと、クラウド上にあるデータはダウンロードすることができますか？")
    )
