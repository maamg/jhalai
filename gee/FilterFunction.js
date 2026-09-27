
var geometry = /* color: #98ff00 */ee.Geometry.Point([88.81832280396388, 23.42322746183498]);
Map.centerObject(geometry, 10);

var s2 = ee.ImageCollection('COPERNICUS/S2_HARMONIZED');

var filtered = s2.filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 30));

var filtered2 = filtered.filter(ee.Filter.date('2019-01-01', '2020-01-01'));

var filtered3 = filtered2.filter(ee.Filter.bounds(geometry));

var filteredefsf = s2
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 30))
  .filter(ee.Filter.date('2019-01-01', '2020-01-01'))


// Exercise
// Delete the 'geometry' import
// Add a point at your chosen location
// Change the filter to find images from September 2023