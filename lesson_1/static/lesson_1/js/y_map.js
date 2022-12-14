ymaps.ready(init);
function init() {
    let map = new ymaps.Map('MapID',{
        center: [60.03345391320664,30.296734646413018],
        zoom:17
    });

    let placemark = new ymaps.Placemark([60.03345391320664,30.296734646413018], {}, {

    });

    map.controls.remove('searchControl');
    map.geoObjects.add(placemark);
}