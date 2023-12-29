from rasa.model_training import train

config_path = "./config.yml"
domain_path = "./domain.yml"
data_path = "./data/"

# Train the Rasa model
train(
    config=config_path,
    domain=domain_path,
    training_files=data_path,
    output="./model/",
    fixed_model_name="restage"
)
