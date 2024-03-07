from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories: list[Category] = []
        self.documents: list[Document] = []
        self.topics: list[Topic] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def edit_category(self, category_id: str, new_name: str) -> None:
        try:
            category = next(filter(lambda c: c.id == category_id, self.categories))
        except StopIteration:
            return

        category.edit(new_name)

    def edit_document(self, document_id: str, new_file_name: str) -> None:
        try:
            document = next(filter(lambda d: d.id == document_id, self.documents))
        except StopIteration:
            return

        document.edit(new_file_name)

    def edit_topic(self, topic_id: str, new_topic: str, new_storage_folder: str) -> None:
        try:
            topic = next(filter(lambda t: t.id == topic_id, self.topics))
        except StopIteration:
            return

        topic.edit(new_topic, new_storage_folder)

    def delete_category(self, category_id: int):
        try:
            category = next(filter(lambda c: c.id == category_id, self.categories))
        except StopIteration:
            return

        self.categories.remove(category)

    def delete_document(self, document_id: int):
        try:
            document = next(filter(lambda d: d.id == document_id, self.documents))
        except StopIteration:
            return

        self.documents.remove(document)

    def delete_topic(self, topic_id: int):
        try:
            topic = next(filter(lambda d: d.id == topic_id, self.topics))
        except StopIteration:
            return

        self.topics.remove(topic)

    def __repr__(self):
        return "\n".join(str(d) for d in self.documents)
