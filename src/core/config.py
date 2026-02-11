# Configuration for Image Conversion Profiles

# Quality Settings
quality_settings = {
    'low': 50,
    'medium': 75,
    'high': 90,
}

# Conversion Profiles
conversion_profiles = {
    'default': {
        'format': 'webp',
        'quality': quality_settings['medium'],
    },
    'thumbnail': {
        'format': 'webp',
        'quality': quality_settings['low'],
    },
    'high_quality': {
        'format': 'webp',
        'quality': quality_settings['high'],
    },
}