const path = require("path");
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

const headerTxt = '/* https://eeia-moteur-recherche.herokuapp.com\nCopyright (c) ' + new Date().getFullYear() + ' EEIA\nVersion: generated at ' + new Date() + '\n*/';

module.exports = {
  context: __dirname,
  name: 'production config',
  mode: "production",
  entry: './static/js/index',
  output: {
    path: path.resolve('./static/dist/'),
    filename: "[name]-[hash].js",
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    // supprimer les codes de debuggage React
    new webpack.DefinePlugin({
      'process.env': {
        'NODE_ENV': JSON.stringify('production')
    }}),
    new webpack.BannerPlugin({
      banner: headerTxt
    }),
    new MiniCssExtractPlugin(),
    new CleanWebpackPlugin(),
  ],
  optimization: {
    minimizer: [new UglifyJsPlugin()],
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader', // translates CSS into CommonJS modules
          'sass-loader' // compiles Sass to CSS
        ]
      }
    ]
  },
  resolve: {
    extensions: ['', '.js', '.jsx']
  },
}
