# κ=0真实接口的完整物理角trace

仅把R630既有物理φ公式作用于真a425接口，不重证通用公式、不再积分、不作材料角重展开。输入为a′>0取向，r=a，w=√(1−a′²)/a′，h_r=h_s/a′。保留全部320个物理模，保存ρ、P̃、K及h、h_r、h_rr的全部系数；h_rr来自实际保存的JVP二阶jet，不以参考轴对称高度代替。另存真实R/T平面系数，方便后续核对完整端圈。

正确标量仍为ed6 HoldProfile。接口s=1.0283496328972757，r=1.1810986109937334，w=2.2110758238987938；数学κ=0故参考w_r=0，浮点评估−1.77694787154e−13。

8192角实际诊断：

|量|值|
|---|---:|
|物理φ高度均值|1.004968957586056|
|K的物理φ均值|.03526393715632481|
|h_r、h_rr均值|2.28904706280063，.5455943216091067|
|ρmin|.16601843096428737|
|max abs(P)、max abs(P̃)|.0784583096125，.296568363233|
|max abs(K)|.395745464235|
|Smin、Dmin|.969905636249，.0357847428454|
|Lmin|.420684828002|
|ymin、Nmin|.604254535765，.457375930853|
|字面Q_φ(ρB)|1.40835910468e−9|

这是有限IVP实际trace：正分支/均值为采样数值，继承原场的有限度量误差。特别地，κ_ref=0不意味着真实非轴h_rr或其均值为0。此处没有非线性DN、精确解或闭合宣称。

S为本题scripts目录，实际命令：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$S" python "$S/parallel_20261117_hold_interface_trace.py" --input parallel-negative-hold-type-interface.json.gz --hold-source "$S/parallel_20261117_negative_hold_profile_ivp.py" --out parallel-negative-hold-type-interface-trace.json --angles 8192
```

SHA256：输入`a425e38ed4caeebf4d1f96629721c2ba1f54d72eef863ac278e7fb64f0327ba8`；本源`9c945d91837f5aa9b573b4ea78f687390ff9e6b6b69f60135fb3a93ede2238ec`；正确标量源`ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1`；完整trace输出`8a956b175f05491afed27896d6a481c643ae10bbe24d832f2572a3b07916f1b1`。输出raw仅scratch。
