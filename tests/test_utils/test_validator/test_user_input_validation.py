from src.config.prompts import PromptsConfig
import src.utils.regex_pattern
from src.utils.validator.user_input_validation import UserInputValidation

# @pytest.mark.parametrize()
def test_input_name(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Aayushi Sharma")
    monkeypatch.setattr(PromptsConfig, "INPUT_NAME", value='')
    monkeypatch.setattr("src.utils.regex_pattern.input_validation", lambda a,b : True)
    assert UserInputValidation.input_name() == "Aayushi Sharma"

# def test_positive_input_username(monkeypatch):
#     monkeypatch.setattr(PromptsConfig, "USERNAME_FORMAT", value="")

