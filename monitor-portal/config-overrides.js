const {
  override,
  fixBabelImports,
  addLessLoader,
  addBabelPlugin,
} = require("customize-cra");

module.exports = override(
  fixBabelImports("import", {
    libraryName: "antd",
    libraryDirectory: "es",
    style: true, // change importing css to less
  }),
  addLessLoader({
    lessOptions: {
      javascriptEnabled: true,
      modifyVars: {
        "text-color": "#455A64",
        "primary-color": "#1DA57A",
        "border-radius-base": "4px",
        "border-color-base": "rgb(225, 227, 229)",
      },
    },
  }),
  addBabelPlugin(["jsx-control-statements"])
);
