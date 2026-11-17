# 原1800预算内全部solver评价点覆盖准备失败

只从原7feed9准备场和真a425接口出发，保同一HoldProfile、原二jet参考函数及54ee88完整BA/BB/非零target；没有读取1396失败场。对原solver的中点及两个RMS位置的坏胞并集二分，新节点仍读原二阶参考，原827节点全部0/1/2jet逐位不变。

本次按实际`create_spline`及`x_middle±h sqrt(3/7)/2`构造solver评价点，RHS仍N2048，域检查用包含该网格的8192角。未改任何RHS或边界，不调用QR或Newton。原题预算1800保持。

|层|节点|坏胞并集|中点Hmin|左RMS Hmin|右RMS Hmin|
|---|---:|---:|---:|---:|---:|
|0|827|234|6.54549e−9|−9.19054e−4|−2.05211e−4|
|1|1061|468|4.58699e−7|−5.51553e−4|−6.10758e−5|
|2|1529|936|4.05675e−7|−2.61663e−4|−1.44758e−5|

三层节点和中点均保持采样域正，但两个RMS组仍失败。下一层同规则必须至少1529+936=2465节点，超过1800，故按原有限预算停止，**没有启动第二次BVP**。节点完整ODE系数缺陷始终.327039521615，相对向量RMS .0279365261883；仅加网格没有解决参考曲线本身的方程缺陷。

这里有具体的插值解释。在二次参考y_ref上令e_L=f_L−y_ref′(左)、e_R=f_R−y_ref′(右)，solver实际Hermite相对参考的偏差是

\[
h\{u(1-u)^2e_L-u^2(1-u)e_R\}.
\]

中点只读h(e_L−e_R)/8；两端缺陷近似相等时该项抵消，而RMS位置仍含一阶h的共同缺陷项。因此中点可通过而RMS不通过，本例不能以只核中点替代完整评估位置。

输出准备标志`passed=false`、`prepared=false`、`new_BVP_solved=false`。本结论只排除此原参考下的指定二分规则/1800预算，不排除同g的解、其他初猜或其他合法网格。

## 复现

S为本题scripts目录：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$S" python "$S/parallel_20261117_hold_bvp_cover_prepare.py" --warm parallel-hold-m160-bvp-adaptive-warm.json.gz --interface parallel-negative-hold-type-interface.json.gz --arrays parallel-hold-m160-bvp-adaptive-arrays.npz --hold-source "$S/parallel_20261117_negative_hold_profile_ivp.py" --output-warm parallel-hold-m160-bvp-allpoint-warm.json.gz --out parallel-hold-m160-bvp-allpoint-prepare.json
```

本源SHA256 `df5795c9831f2142d6b786b37d96f8420304f6a5c1cfb6ea937e867dcaed83d4`；输出warm `3a1155d7e505dd23f2325aed941c53ae6a1ed16a4cca84c36f9508cc0dbadffa`；实际report `2d934568170c8bbc9610202aa7c5e93ff07b5cb2af9dcc61b5e32c0ad32530b5`。report完整保存每层/每组坏胞编号、Q/W/H和ODE缺陷，绑定原warm、a425、54ee88、ed6及实际SciPy backend SHA，raw只在scratch。
