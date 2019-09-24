const VueLoaderPlugin = require("vue-loader/lib/plugin");
const TerserPlugin = require('terser-webpack-plugin');
const CopyPlugin = require('copy-webpack-plugin')

module.exports = {
    // モード値を production に設定すると最適化された状態で、
    // development に設定するとソースマップ有効でJSファイルが出力される
    mode: "production",
  
    // メインとなるJavaScriptファイル（エントリーポイント）
    entry: "./src/main.ts",
    output: {
      //  出力ファイルのディレクトリ名
      path: `${__dirname}/dist`,
      // 出力ファイル名
      filename: "main.js"
    },
    module: {
      rules: [
        { 
            test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/, 
            loader: "url-loader?limit=10000&mimetype=application/font-woff" 
        },
        { 
            test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/, 
            loader: "file-loader" 
        },
        {
            test: /\.vue$/,
            loader: 'vue-loader'
        },
        {
            test: /\.(jpg|jpeg|png)$/,
            loader: 'url-loader'
        },
        {
            // 拡張子 .ts の場合
            test: /\.ts$/,
            // TypeScript をコンパイルする
            use: "ts-loader"
        },
        {
            test: /\.js$/,
            exclude: /node_modules/,
            loader: "babel-loader"
        },
        {
            test: /\.s[ac]ss$/i,
            use: [
                'vue-style-loader',
                'css-loader',
                'sass-loader',
            ]
        },
        {
            test: /\.css$/,
            use: [
                "vue-style-loader",
                "css-loader",
            ],
        },
      ],
    },
    plugins: [
        new VueLoaderPlugin(),
        new CopyPlugin([{ from: './public' }])
    ],
    optimization: {
        minimize: true,
        minimizer: [new TerserPlugin({
        terserOptions: {
          ecma: 6,
          compress: true,
          output: {
            comments: false,
            beautify: false
          },
          sourceMap: false
        }
      })]
    },
    // import 文で .ts ファイルを解決するため
    resolve: {
      extensions: [".ts", ".js", ".vue"],
      alias: {
        // vue-template-compilerに読ませてコンパイルするために必要
        vue$: 'vue/dist/vue.esm.js',
      },
    },
  };