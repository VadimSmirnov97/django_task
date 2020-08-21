axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
new Vue({
        el: '#app',
        data: {
            id: '',
            text: '',
            status: '',
            loading: false
        },
        methods: {
            solveTask() {
                this.getTextArea()
                this.loading = true
                this.status = ''
                var form = new FormData();
                form.append('text', this.text);
                axios.post('/add_task/', form).then(response => {
                    this.id = response.data['task_id'];
                    var time = setInterval(() => {
                        axios.get('check/' + response.data['task_id']).then(response => {
                            this.status = response.data['status']
                            if (response.data['status'] !== 'evaluation'){
                                this.loading = false
                                clearInterval(time);
                            }
                        }).catch(function (error){
                            console.log(error)
                            clearInterval(time)
                        })
                    }, 500)
                }).catch(function (error){
                    console.log(error)
                });
            },
            getTextArea() {
                this.text = codeMirror.getValue()
            },
        },
}
)


var codeMirror = CodeMirror.fromTextArea(document.getElementById('codeeditor'), {
    theme: "material-ocean",
    lineNumbers: true,
    tabSize: 4,
    indentWithTabs: true,
    autoRefresh: true,
})