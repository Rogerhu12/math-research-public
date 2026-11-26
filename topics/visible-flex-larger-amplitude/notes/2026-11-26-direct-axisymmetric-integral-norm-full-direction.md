# 2026-11-26：同固定R690目标的原完整606积分范数新方向

## 1. 选择与范围

本次准备直接使用已经公开的完整606e driver，在仍活动的公开Run03b上执行 **norm-kind=integral、无restart、1个完整64内层度量方向、至多4个完整64内层Phase I方向**。它从同一真实独立轴对称参考的q.initial建立新初点，使用同固定标量目标、完整原变量、全部正权E/交叉/G残差、完整J/J*、原几何选择机制、全部幅度约束和全点真实验收。

这是一项**同固定g的新初点和新完整坐标范数选择**。它不保留第3步末fbf2或第17步末b1c的当前自由点，不称同x对照；也不从旧jet-sum范数自动转换或继承阻尼。新的metric和restoration初始阻尼均明确指定为0.01，仅是本次积分坐标下的新算法常数，不宣称与旧0.01正则化同量级或最优。

不改任何科学源或原source guard。原606完全不含359f的SOC步骤，因此本次不混入旧alpha=0.5固定锚修正，也不冒称已接Run04新后退锚算法。归因使用其原6d54纯reader。

## 2. 为什么这是一项有根据的后继，而不是已有结论

[Run03b第17/18步的完整实际返回](2026-11-26-actual-SO3-prior-separation-SOC-17-18.md)记录了cell0/1相关真实几何拒绝、有限行修正与全场验收之间的差距，以及最终原ray的极小接受步长。这些实际现象本身没有证明其全部原因是径向胞长度或某一种范数。

独立解析材料[节点jet范数与径向积分控制](2026-11-26-node-jet-norm-and-radial-integral-control.md)给出一个准确反例：在逐渐缩短的共享五次胞上，正节点jet范数不提供与网格无关的径向H²控制。它提出了一个值得实际检验的算法原因；它不证明已经返回的任一QP方向就是该反例，也不能把所有真实失败归因于它。

当前原完整RotationH2Coordinates早已提供integral分支。它保留全部自由量，并直接支付径向多项式内部的一、二阶导数积分，故这次可以只选择现有完整范数，而不删变量、不冻结core/H、不替换原度量约束，不另外建立可选小fixture。原integral分支没有已登记的实际Cholesky失败；不能先把数值失败预填，也不要求先运行另一个QR方案作为前门。

积分范数的完整正定性、白化与转置边界见[积分SO3范数与带状QR解析说明](2026-11-26-integral-so3-norm-positive-whitening-and-banded-qr.md)。本条不重复登记那一数学结论，也不声称新数值效果已经得到。

## 3. 实际固定输入与完整来源

本次仍使用Run03b实际准备输出：

| 对象 | 已实际绑定身份 |
|---|---|
| reference.npz | 0f0424cc7403d0ffbca22490fc9d0bc154c52c356278a800553528e77fc386c1 |
| fixed scalar g | 6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb |
| 原完整direct-SO3 model | 9d4ccb16efe9a0c0f5b077c0e8919e76d1d04b06e669588b32e2de78c92f0258 |
| 原第3步完整报告 | 989740cd8408c317b4540c3efa82b6ab35de269dcb200932f4d1d19d370773d1 |
| 原第17步完整报告 | cd1af889cb1b4f6fb71c6100ddebd7e5ccdadcd04ae5fe1df457f6279507017a |

数值输入路径保持axisymmetric-R690-reference-v2-first/{reference.npz,report.json,observations.npz}，node/scalar输入保持fullclosed_solver/data/{fullclosed-hold-warm.json,pulse-a5-complete-base.json.gz}。所有实际文件仍由原launcher和driver重新绑定；本说明不代替这些运行时核查。

| 原完整源码 | SHA256 |
|---|---|
| fullclosed_axisymmetric_so3_qp.py | 606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9 |
| launch_axisymmetric_so3_actions.py | a94263f037dfa8535b11cf44fa93b6a4cd6df7dee1a6be35f2ea14f5abaa2690 |
| read_axisymmetric_so3_report.py | 6d54cbba7ff998bc98b0f39c6a26ae33c16957fb0b9dc0fffced1037212455eb |
| so3_axisymmetric_meridian_operator.py | 7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf |
| so3_axisymmetric_meridian_geometry.py | 2240a1f68021991a85c502ed3cf67c82f6bac6e1e4e10b3b3286eab120d4f229 |
| so3_axisymmetric_reference.py | 4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3 |

原闭合源码表的所有其余行也保持原样；没有以新路径冒用旧函数身份。

## 4. 完整范数、自由量与单位

原integral分支使用

$$
\|\delta x\|_I^2
=
\sum_m\sigma_m^2
\int_0^S
\left(
\delta\omega_m^2+
\ell^2\delta\omega_{m,s}^2+
\ell^4\delta\omega_{m,ss}^2
\right)ds
+
\sum_{\nu\ \mathrm{free}}((1-\nu^2)\delta c_\nu)^2
+
(\delta H)^2,
$$
其中ell=0.05，角向transition=24。全部原旋转模式、共享五次径向自由jet、全部free core和H都保留，有限自由量仍为1,333,370；相应完整正权度量行仍为45,324,288。Phase I只有原公共slack增广，不删物理自由量。

原实现使用每胞6点正Gauss组装完整三项多项式积分。对共享五次多项式，最高平方次数10，6点Gauss在精确算术下支付该完整多项式；实际浮点组装/Cholesky仍是工作实现，不自动成为严格算术证书。原带宽5、对角平衡、完整带状Cholesky与完整lift/transpose均保持，报告会给出本次实际band、factor、equilibration与新norm_identity。factor失败则按原真实错误返回，不替换成jet-sum，不剪裁负特征，不把数值分解失败称数学不可能。

本次只按明确命令使用metric_mu=0.01、restoration_mu=0.01。因为范数本身改变，旧norm_identity、旧coordinate_step、旧Pg/tolerance、旧方向预测和旧阻尼路径均不作为本次数值依据。标量目标损失仍是p4/epsilon0.001/scale0.05的同固定g损失；只允许本次新初读与本次末读按同Phi比较。

## 5. 全部历史地址如何进入原606

ready只列出已经真实返回、可用的三份完整地点源：

1. axisymmetric-R690-reference-v2-first/locations.json；
2. axisymmetric-so3-complete-v2-first/report.json；
3. axisymmetric-so3-prior-separation-SOC-first/report.json。

第18步只是第17步完整报告的纯读取，不是一个新的原始地点manifest；因此不把其归因输出冒充科学位置源。第17步完整报告保留自己的完整起点历史、所有真实trial/分离/SOC地址以及最终curvature/radius memories。这些地址进入原606的all_locations，再由原history.Locations.walk处理，不继承任何旧场数值或几何certificate。

这一用法只采用已经存在的原walker协议：

- 每个输入必须声明与当前observations.npz逐字相同的carrier SHA；
- 凡有tagged grid index，必须显式声明与当前一致的N/full_angles/full_N，仍为2048；
- 由当前同carrier解析grid地址，任意点使用cell和literal binary64 u/phi，地址不作十进制舍入；
- 固定材料角始终是同一初始reference的phi0，不是当前内部逆图phi_c；
- protected地点、curvature和radius两集合按原规则保留；两距离符号仍由完整真筛读取。

因此从旧报告继承的是同固定chart的**位置**，而不是旧约束梯度、旧C行、旧真假判断或旧Phi。每个新方向都在本次真实父点、使用新积分坐标的完整T*重新生成其C；原几何选择机制及幅度追加不被新历史报告替换。全部永久位置的真筛仍独立于有限C选择。

R696角向新表示在本说明编写时仍未返回，本ready不假填其pending报告。若它先实际返回且需要在本次执行前追加，必须保持同carrier/N/mesh及同固定材料phi0语义，再把其真实完整报告作为新的明确manifest参数加入，并记录更新后的参数文件hash。数学上不同场可以共享同固定域地址，但不能由相同文件名或相同N单独推出这种同一性。此处是已存在输入协议的适用说明，不新增科学fixture或执行前验证门。

## 6. 可执行两步与完整参数

完整参数文件为[resume-20261126-direct-integral-norm-full64-ready.json](../computations/resume-20261126-direct-integral-norm-full64-ready.json)，22083字节，SHA256 **104af2b654f1cfa0673a0c473e31aa1ae2bd878727bf2bb20408a129da90e957**。它是一份含两个完整step对象的JSON数组，可由根代理追加到原03b队列；本代理未修改队列或触发Actions。

第一步执行原完整launcher，fresh输出axisymmetric-so3-integral-norm-first；第二步执行原完整6d54 reader，fresh输出postprocess/axisymmetric-so3-integral-norm-first-readout.json。

| 参数 | 明确值 |
|---|---|
| 物理初点 | 无restart；真实q.initial，保原参考H，不另改H |
| norm / ell / angular transition | integral / 0.05 / 24 |
| metric directions / maxiter | 1 / 64 |
| restoration directions / maxiter | 4 / 64 |
| 新metric / restoration damping | 0.01 / 0.01 |
| 同损失 | p4、epsilon0.001、scale0.05、centered标量 |
| N / stage block / angle block | 2048 / 64 / 8 |
| 工作径向积分阶数 / panels | 8 / 128 |
| 逆图工作迭代 / 容差 | 18 / 2e-12 |
| 线程 | 4 |
| QP atol / rtol / feasibility / rank | 0 / 1e-6 / 2e-11 / 2e-12 |
| 原几何选择预算 / block columns / active band | 192 / 32768 / 0.025 |
| ray trial上限 | 15 |
| reach ratio / 原安全系数 | 0.03 / 0.992 |
| marked D / witness L / H floor | 4.2 / 0.9 / 1.01 |
| amplitude top radius / distance | 2 / 4 |
| legacy fraction | 0.5 |
| solver数值target | 1e-9，不是完成证书 |

使用的Phase I仍是原606公共slack算法和原真实物理验收；没有偷带normalized-parent 0f的内缩修订。初点是否通过所有新增历史位置必须真实重读，不能引用第3步旧初点有限通过结果。若恢复预算结束仍有真实g>0，则如实返回并继续处理，不称该点可行，也不把slack下降称几何通过。

清理仅限本步新生fixed-axisymmetric-reference-cache与rows-*，由既有控制器在子进程自然返回后按原保护规则执行；输入、完整report、initial/final NPZ和命令报告不删。没有跨runner raw迁移或重跑旧方向。

## 7. 实际静态检查及归因责任

本地仅做了原完整源码的SHA/AST、参数JSON、原3cb1队列_validate_queue，以及原a942 launcher的--print-command。全部实际通过；生成命令指向原606完整body，norm-kind=integral，maxiter=64，三个manifest且无restart。没有本地F/J、范数组装、分解、QP、科学数组或fixture执行。

pure reader保留原完整来源、fixedg、canonical norm和同Phi核查。ready除记录完整norm与真实初/末场外，直接公开第一个真实度量方向的QP status、advances、Pg、tolerance、alpha、全部15个可能ray的标量归因及至多4个恢复方向。没有发生的方向/trial应在控制器summary_errors明确缺失，不用零值填充，不从预算推断收敛。

若实际factor或首场读取未成功，原报告可能尚未生成；必须读取真实trace，不依据“计划integral”填成功或失败原因。若原完整数值方向成功返回，也仍须继续追踪同固定目标下的实际误差下降、非线性全筛、可复现精化与最终连续证书。当前这两步尚未科学运行，本条不预填任何效果。

## 8. root实际追加与已返回R696地址

2026-11-26 16:43:49 UTC，root亲读实际21/22：完整399ae8报告/4aa387末场同0f042/6ffc/b025/N2048；相同reference源码4e655读同mesh及材料phi0，故依原walker只迁位置，在新点用新T*重建全部值/C。将其完整report作为第四manifest；没有继承其场或真假判断。原三manifest准备版本104af2保历史；现完整ready 22460B，SHA `a177a815e29e82166fae2f67445a9b641e393dcd8fb3f0ba4becaa3d7311468f`。全部其余科学argv和源不变。

原3d9详细pure读取参数3e332/25783B放在此完整方向之前，读取实际21唯一方向及全部已实际ray；未发生项由summary_errors记缺，不能预填驻点。03b的14–20完整原queue字节65711B/3d856原样归档archive002，原archive001链保，19的真实失败不改成功；21–24所有对象原样保，controller attempted阻止重做。当前活动文件76310B/fb55187c1d2ef6ef4c94a4e1eda1de4ffceb405fe8819b9dbee14d2ff5ddb013。

完整积分正定/转置/流式QR解析说明也已刊；root通读全证并核官方band布局/LAPACK接口。QR小源是独立备选，原606这次实际方向不等待它。只做源码/参数/元数据核，没有本地范数组装、分解、F/J或科学fixture。
