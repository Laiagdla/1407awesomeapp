run_api:
	uvicorn awesomeapp.simpleapi:api --port=5050 --reload

run_st:
	streamlit run app.py

############### build and run locally ####################3
build-local:
	docker build -t dummyapp:dev .

run-local:
	docker run -p 8000:8000 --env-file .env dummyapp:dev

run-interactive:
	docker run -it -p 8000:8000 --env-file .env dummyapp:dev sh
