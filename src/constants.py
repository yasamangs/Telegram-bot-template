from types import SimpleNamespace

from src.utils.keyboard import create_keyboards

# basic keys for creating a Bot
# you can add your intended emojis' text along as well
keys = SimpleNamespace(
    start='Start :grinning_face_with_smiling_eyes:',
    settings='Settings :gear:'
)

keyboards = SimpleNamespace(
    main=create_keyboards(keys.start, keys.settings)
)
