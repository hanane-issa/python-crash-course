window.addEventListener('load', () => {
  if (window.thebe) {
    window.thebe.on('kernelReady', () => {
      document.querySelectorAll('.thebe-cell .CodeMirror').forEach(cmElem => {
        const cmInstance = cmElem.CodeMirror;
        if (cmInstance) {
          cmInstance.setOption('theme', 'material-darker');  // built-in dark theme
        }
      });
    });
  }
});
