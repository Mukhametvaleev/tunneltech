const path = require('path');

const { WebpackManifestPlugin } = require('webpack-manifest-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = {
    context: path.resolve(__dirname, 'src'),
    entry: ['./index.tsx'],
    devtool: 'source-map',
    mode: 'development',
    module: {
        rules: [
            {
                exclude: /node_modules/,
                test: /\.(ts|tsx)?$/,
                use: ['babel-loader', 'ts-loader'],
            },
        ],
    },
    plugins: [new CleanWebpackPlugin(), new WebpackManifestPlugin()],
    resolve: {
        extensions: ['.ts', '.tsx', '.js'],
    },
    output: {
        path: path.resolve(__dirname, 'static/frontend/'),
        filename: '[name].[hash].js',
        publicPath: '',
    },
};
