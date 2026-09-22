# AgriSmart datasets

Place approved datasets here during local development.

## Crop recommendation schema

CSV columns:
N,P,K,temperature,humidity,ph,rainfall,label

## Plant disease schema

Use a directory-per-class image dataset, for example:

dataset/
  train/
    Tomato___Healthy/
    Tomato___Late_blight/
  validation/
    Tomato___Healthy/
    Tomato___Late_blight/

## Yield prediction schema

CSV columns should include:
crop_name,area_acres,rainfall,temperature,soil_ph,yield
