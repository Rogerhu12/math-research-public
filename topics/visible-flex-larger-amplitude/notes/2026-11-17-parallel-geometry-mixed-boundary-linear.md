# 645/317 短段混合边界的实际负诊断

**有限线性证据；没有新 BVP 或父场。** 本条使用已成功的 M320/N4096 `.995→.997` 公共五次场（129 节点共同 value/rhs/d2），不使用失败的至 `1.0` Cauchy 轨迹。完整 raw SHA256 为 `507cab03af49bf58305cd9e91421e2b91c0071cc4115dd8e1f6d1f047ad9389a`，定义见 [完整短段记录](2026-11-17-parallel-geometry-m320-full-short-quintic.md)。原标量和原 core 的 rho 均保留。

## 定义与计数

沿用 [实际移动框架](2026-11-17-parallel-geometry-frenet-schur-diagnostic.md)：`Tδy=P_M(δF·es,δF·eφ,δF·n)`，`Ts` 取同一参考真实 jet。坐标为 `(p0..320,t1..320,w0..320)`。固定所有 p/t 及 w0..3 共645行，释放 w4..320 共317列；`U=T0⁻¹E`，E 为单位阵最后317列。这里只固定有限投影分量，不保证高频切向泄漏逐点为零。

取完整有限 `A(s)=Dy f(y*(s),a′/a)`，末端 `B1=(T1 A1+Ts1)T1⁻¹`。按实部切口 `1.59014376→4.68866670` 选 B1 的快速左实 Schur 行 LB，实际恰317维，无共轭块删切；令 `L=LB T1`。两端 cond(T)=1.25586/1.25507，选区实部至1290.18874、最大虚部239.888645；相对左不变性残差1.715e−15。但分离估计仅.0090137，斜谱投影范数2405.65，不能把实部隙当稳定性证书。

令 tail 为真实末点旋转 Fourier 的 m225..320 全 R/T/Z 分量。**删模只定义目标** `b=−L tail`。全部962 ODE的317列变分为 `Y′=AY,Y0=U`，求完整 `Kη=b,K=LY1`；没有截奇异值或删方向。

## 实算和必要核对

完整 DOP853 传播使用 rtol1e−8/atol1e−11，首步.002/256、最大步.002/64；122节点、1501次RHS。调用点最大参考 ODE 缺陷为1.30417e−11，属抽样记录。

| 量 | 实际值 |
|---|---:|
| σmax(K)/σmin(K)，cond2(K) | .40746936 / 2.55541e−7，1.59454e6 |
| max abs(b) / norm2(b) | 9.26039e−12 / 2.72404e−11 |
| 解的右残差 / 固定左残差 | 4.16075e−23 / 1.37643e−21 |
| 最大自由框架/原系数变化 | 5.24957e−6 / 5.01945e−6 |
| 8192角起点 (δF,δFφ,δFφφ) 最大范数 | (8.83455e−6,.00548488,3.46250) |
| 预测末点同三量 | (5.23816e−6,.00165365,.889802) |
| 线性径向一阶/二阶变化最大范数 | .00885611 / 738.74794 |

独立用 matrix-free `q.jvp` 只传播所求初值方向：步长.002/256、.002/512，容差分别1e−11/1e−18、1e−12/1e−19；3088/6148次RHS。精档真实右行残差范数9.64229e−18，约目标的3.54e−7；两档末系数差9.92532e−16，位置/角二阶差1.85251e−14/3.75024e−9。这核对该方向，未认证整个逆矩阵。

**实际反代起点已失败：** 在8192角上，`Q=|Fφ|²,W=|Fφ×Fφφ|²,H=W−(a′/a)²Q³` 给出 Qmin=.03759031、Wmin=4.55665e−6，但 **Hmin=−.02056612**（φ=1.94278667）。没有在域外伪造实际 RHS/二阶 jet。因此这一 normal-only 自由方向与此目标的完整线性步不可作为新场；不排除其他子空间、目标或非线性分支。

值差也不能省略：附加 `p0(u)=1−10u³+15u⁴−6u⁵` 桥时，其值项一/二阶费用为 `15|δF|/(8w)`、`10|δF|/(√3w²)`。用上述抽样位置范数作数值预算，w=.0005为.03313/204.03，w=.001为.01656/51.01；这些不是完成桥的证明。

## 冻结复现

- [317列源](2026-11-17-parallel-geometry-mixed-boundary-linear.py)：`33c7af360f043decfab2de214981000ed8356c3e302f1e941710fe5ca9967ebe`。
- [单列核对](2026-11-17-parallel-geometry-mixed-boundary-check.py)：`9b3c360519cf499b94dfef5009ee27df83e1e11fcc4d5213878ed48435b5230f`。
- 已有 Schur helper：`426635e625e3f80b2b7eea238df1a7f9ac9285fafa5f87a79fd0e2c3d645cd6b`。

仓库外报告 `parallel-geometry-mixed-boundary-linear-report.json` SHA `c34c9ad08dff644dd8876c1ca1d27137e04cc29c502357dad393fe85b3109e41`；`parallel-geometry-mixed-boundary-check-final-report.json` SHA `dfb177b50796bbc81228ee35405544314d3acb1a42b38337b94bb2b70187ae5a`。

两次命令均设 `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1`。先运行 linear.py，传 `--topic TOPIC --field RAW --out REPORT --target-cutoff 224 --read-angles 8192 --rtol 1e-8 --atol 1e-11`；再运行 check.py，传 `--topic TOPIC --field RAW --linear-report REPORT --out CHECK`。RAW 为上述507cab完整场；报告含计时，复算不要求字节同一。未得到(.997,1.0]新场、全相位共同g、闭合、reach或完成标准。
