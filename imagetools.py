import argparse

import MapDatumTrans

from tools.dms_dd import dd2dms
from tools.image_gps import modify_image_gps


def write_gps_info_to_img_file(args):
    if args.to_gcj02:
        latitude, longitude = MapDatumTrans.wgs84_to_gcj02(args.latitude, args.longitude)
    else:
        latitude = args.latitude
        longitude = args.longitude

    north_or_south, longitude_degrees, longitude_minutes, longitude_seconds, east_or_west, latitude_degrees, \
        latitude_minutes, latitude_seconds = dd2dms(latitude, longitude)

    modify_image_gps(args.image, north_or_south, latitude_degrees, latitude_minutes, round(latitude_seconds * 100),
                     east_or_west, longitude_degrees, longitude_minutes, round(longitude_seconds * 100))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='imagetools')
    parser.add_argument('--foo', action='store_true', help='foo help')
    subparsers = parser.add_subparsers(help='sub-command help')

    # ------- SUB COMMAND for Write GPS information to image file. -----------------------------------------------------
    parser_wgpsimg = subparsers.add_parser('wgpsimg', help='Write GPS information to image file.',
                                           usage='%(prog)s xxx.jpeg [options]')
    parser_wgpsimg.add_argument('image',
                                help='A image file, such as my_photo.jpg')
    parser_wgpsimg.add_argument('-la', '--latitude',
                                type=float,
                                metavar='',
                                required=True,
                                help='Decimal degrees latitude, such as: 22.578829')
    parser_wgpsimg.add_argument('-lo', '--longitude',
                                type=float,
                                metavar='',
                                required=True,
                                help='Decimal degrees longitude, such as: 114.219687')
    parser_wgpsimg.add_argument('-tg', '--to-gcj02',
                                action='store_true',
                                help='Whether convert the GPS info from WGS84 to GCJ02')
    parser_wgpsimg.set_defaults(func=write_gps_info_to_img_file)

    # ------- SUB COMMAND for Turn WGS84 GPX file to GCJ02 GPX file. ---------------------------------------------------
    parser_gpxw2g = subparsers.add_parser('gpxw2g', help='Turn WGS84 GPX file to GCJ02 GPX file.')
    parser_gpxw2g.add_argument('--baz', choices='XYZ', help='baz help')

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
