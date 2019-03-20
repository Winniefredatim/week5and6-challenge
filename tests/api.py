from flask.views import MethodView
from flask import jsonify, request, abort

from diaryStore import store

class DiaryApi(MethodView):

    def get(self, diary_page_id):

        # check if diary_page_id is part of the endpoint url
        if diary_page_id:
            for diary_item in store.diary:
                # if diary_page_id equals id of diary in diaryStore list, then return it
                if diary_item['id'] ==diary_page_id:
                    return jsonify({'diary_item': store.diary[diary_page_id - 1]}), 200
            else:
                # if no diary_page is found
                return jsonify({'error': f'diary_item with id {diary_page_id} not found'}), 404

        # if diary_page_id is not part of endpoint url, return all mydiary
        if not store.diary:
            return jsonify({'Mydiary': 'No mydiary yet'}), 200
        return jsonify({'Mydiary': store.diary}), 200

    def post(self):
        # adding  diary_item to mydiary list
        if not request.json or not 'page' in request.json:
            abort(400)
        diary_item = {
            'id': len(store.diary) + 1,
            'page': request.json['page'],
            'title': request.json['title'],
            'description': request.json['description'],
            'date': request.json['date']
        }
        store.diary.append(diary_item)
        return jsonify({'diary_item': diary_item}), 201

    def put(self,diary_page_id):
        # updating diary_page
        if not request.json or not 'page' in request.json:
            abort(400)
        diary_item = store.diary[diary_page_id - 1]
        diary_item['page'] = request.json['page']
        diary_item['title'] = request.json['title']
        diary_item['description'] = request.json['description']
        diary_item['date'] = request.json['date']
        return jsonify({'diary_item': diary_item}), 200

    def delete(self, diary_page_id):
        # deleting diary_item
        del store.diary[diary_page_id - 1]
        return jsonify({}), 204