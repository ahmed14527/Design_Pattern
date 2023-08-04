class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            # put any initialization here
            cls._instance.mode = 'dark'
        return cls._instance

# Trying to get instance of Settings
settings = Settings()  # Does not throw error, returns the singleton instance

another_settings = Settings()  # This also returns the same instance

# Proving that both variables are pointing to the same instance
print(settings is another_settings)  # prints: True


print(settings._instance.mode)
print(another_settings._instance.mode)