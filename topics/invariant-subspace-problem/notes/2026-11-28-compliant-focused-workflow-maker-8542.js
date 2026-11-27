return function(name,group,file,deps=[],seconds=195){
let wf=load("isp_simple_workflow_template_recovered");
wf=wf.replace(/^name:.*$/m,"name: "+name).replace(/group: .*/,"group: "+group).replace(/ISP_FILE: .*/,"ISP_FILE: "+file)
.split("\n").filter(l=>!l.includes("git show")||l.includes("$ISP_SOURCE_PATH")||l.includes("2026-11-27-focused-exact-actions-driver-8542.py")).join("\n");
const stage=deps.length?['          git show "$ISP_PIN:topics/invariant-subspace-problem/notes/2026-11-28-load-historical-input-8542.py" > "$RUNNER_TEMP/isp-history-loader.py"',
 ...deps.map(d=>'          python "$RUNNER_TEMP/isp-history-loader.py" --repo "$PWD" --ref "$ISP_PIN" --path "topics/invariant-subspace-problem/notes/'+d+'" --output "$RUNNER_TEMP/'+d+'"')].join("\n")+"\n":"";
wf=wf.replace('          python -u "$RUNNER_TEMP/isp-equal-six-driver.py"',stage+'          python -u "$RUNNER_TEMP/isp-equal-six-driver.py"').replace("--seconds 195","--seconds "+seconds);
return wf;
};