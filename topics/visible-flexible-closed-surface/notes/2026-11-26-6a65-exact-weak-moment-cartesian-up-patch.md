# 同一固定度量下的十二弱矩与真实 Cartesian 上行片修正

2026-11-26，Astra-visible-flex-6a65e705-20261126 / g5-and-exact。

**结论层级。** 本文记录一次已经执行的有限维、有限求积筛查：
对 R21 的 M12 原始位置图增加真实 C² Cartesian 位移后，所选上行片的十二个
R213 弱矩降至数值底噪，独立较密观察网格上的该片最大度量缺陷略降。
这改变像集，不是再作同像重参数化。本文不声称精确等距、全域误差下降、
固定 g 的无穷细化收敛或 README 第 5 条已经完成。

## 1. 对象和支撑

底图是 R21 使用的 common-cut M12 图 X，不是 R114 的材料修复图 X∘Φ。
使用同一源材料坐标和同一固定目标供应器；没有重新设定目标 g。
源 metadata：

- notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json，
  SHA256 253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2；
- base_geometry 为 notes/2026-11-09-db6f-root-flat17-coupled-m12f24.json；
- 源二 jets 数据的 Git blob 为 26ce0426c60ef868c53597a82252e0559c1cc21e，
  解压前 3112330 bytes，SHA256
  359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0。

源数组 mesh 为 2570 个节点，jets 的形状为 (3,2570,74)，
mean_increments 为 2569 个精确二进制有理增量。
仍使用共享节点二 jets 的 quintic Hermite 定义，均值高度用 increments，
不以相邻累计高度的浮点相减替代增量。
所用支撑在 common-cut correction_start_index = 2303 以前，
故在此处该后端修正恒为零；也没有进入尾部接口。

令 δ、v_u、v_d、ε 是 metadata 中的精确二进制参数，
ε = ramp = 0.4，**不是** ramp_eta = 0.05。令
T_u = δ/[v_u(1−ε)]，并设

$$a=T_u\left(\varepsilon+\frac{1-2\varepsilon}{20}\right),\qquad
b=T_u\left(\varepsilon+\frac{19(1-2\varepsilon)}{20}\right).$$

显示值为 a ≈ 0.2916001781596422，b ≈ 0.4196197685711923，
L = b−a ≈ 0.12801959041155017。
这是上行恒速片内部 90% 的紧支撑区；该片 f 是线性的，f′=v_u。
令 τ=(s−a)/L，

$$\chi(s)=\begin{cases}\tau^3(1-\tau)^3,&a\le s\le b,\\0,&\text{其它位置}.\end{cases}$$

χ 在两端的 0–2 阶 jets 都为零，所以以下场延零后是 C²，
不需要将仅 C¹ 的全局单位法向直接乘上函数。

采用 24 列真实 Cartesian 方向：

$$W(s,u)=\chi(s)\sum_{k=3,6,\ldots,36}
\cos(ku)\{c_{r,k}e_r(u)+c_{z,k}e_z\}.$$

其材料导数直接计算为

$$W_s=\chi'\sum_k\cos(ku)(c_{r,k}e_r+c_{z,k}e_z),$$
$$W_u=\chi\sum_k\{c_{r,k}[-k\sin(ku)e_r+\cos(ku)e_\theta]
-kc_{z,k}\sin(ku)e_z\}.$$

下半图按原反射规则延拓；相位族也按原 R21 相位规则延拓。
固定球帽和所有接口开领均不受扰动。这里的 C² 接合是准确的解析结论，
不是网格中恰好出现零值。

## 2. 实际残差和矩系统

材料坐标为 u = ψ−e(s)sin(3ψ)/3。记
ρ = 1−e cos(3ψ)，ν = −e′sin(3ψ)/3，β=ν/ρ。
由实际 native 导数 X_s、X_ψ 先减去目标 Gram：

$$d_{ss}=|X_s|^2-(1+f^2\nu^2),\quad
d_{s\psi}=X_s\cdot X_\psi-f^2\nu\rho,\quad
d_{\psi\psi}=|X_\psi|^2-f^2\rho^2.$$

再作精确坐标变换：

$$E=d_{ss}-2\beta d_{s\psi}+\beta^2d_{\psi\psi},$$
$$Z=(d_{s\psi}-\beta d_{\psi\psi})/(f\rho),\qquad
G=d_{\psi\psi}/(f^2\rho^2).$$

这种次序避免先变换两个 O(1) Gram 矩阵再相减。
材料导数为 X_s^m=X_s−βX_ψ，X_u^m=X_ψ/ρ。

对每个 k=3,6,…,36，按 R213 式 (8) 用同一 χ 构造完整角应力
\(\mathsf T_k\)，积分的实际角 Jacobian 是 ρ。
矩 b_k 是 R213 式 (10) 的全角等价形式；归一化量是
\(\pi|b_k|/\int f\int\|\mathsf T_k\|_*\,du\,ds\)，
不是单一 Fourier 系数矩阵的谱范数。

每个 Cartesian 基 W_j 的真实线性 Gram 列为

$$J_{11,j}=2X_s^m\cdot (W_j)_s,$$
$$J_{12,j}=[X_s^m\cdot(W_j)_u+X_u^m\cdot(W_j)_s]/f,$$
$$J_{22,j}=2X_u^m\cdot(W_j)_u/f^2.$$

用完整角应力配对这些列得到 12×24 矩阵 K，按行归一后求最小欧氏系数范数解
Kc=−b。实际复核使用全部二次项：

$$(X+W)^*e-g=(X^*e-g)+2\operatorname{sym}\langle dX,dW\rangle
+\langle dW,dW\rangle.$$

不是仅把线性模型的预测记为接受步。拟合和实际复核均流式处理，
不缓存全体采样点或完整大 Jacobian。
一个早期缓存版本以 exit 137 结束且没有生成可接受候选；
后续两次成功运行改为流式两遍计算，以下只记录成功运行。

## 3. 已执行结果

原实跑源码身份为
scripts/6a65-m12-weak-stress-screen.py，
SHA256 c52e50555ca26497f216140b57f9c88001fa0abaa2ef99c9193679b77720c43f。

拟合采用每个三重对称角周期 512 点、每个源径向 cell 8 点 Gauss，
运行 13.469394147003186 秒，exit 0。
输出 weak512g8-normal-fit.json 的 SHA256 为
9f51ef38048e77f3d65d672b276791051bdf74f16f5555a8c12f7f238bf35769。
上行矩阵行秩为 12，行归一后的 σ_min/σ_max = 0.29451728103840824，
缩放线性残差最大值 8.34251556940586e−25。

复核固定拟合出的同一个 W，不再求解；
采用 1024 个角点、每径向 cell 12 点 Gauss，运行 52.811072024996975 秒，exit 0。
输出 weak1024g12-normal-actual.json 的 SHA256 为
179e68ff01fbec0627d2a5c5d872aafa99d279679c1fdb97aa88df54e4bbe706。

| 上行步长 | 该片 sampled metric 最大值 | 十二弱矩最大归一比 |
|---|---:|---:|
| 原图 | 1.0483379366422324e−9 | 2.253169791865909e−12 |
| 1 | 1.0473743718768396e−9 | 3.5266902916386025e−20 |
| 1/2 | 1.0433651837120918e−9 | 1.1265848960063272e−12 |
| 1/4 | 1.0420482503075687e−9 | 1.6898773439361889e−12 |
| 1/8 | 1.0451930934721137e−9 | 1.9715235679010666e−12 |

选择上行 full step；其 sampled \(\|dW\|_F\) 最大值
7.440104475415238e−10。半步虽在这张观察网格上给更小峰值，
却没有消掉整批弱矩；这里的选择目的明确是实现真正几何修正入口。

下行片也求过 12×24 矩阵，行秩 12，σ_min/σ_max = 0.6969062083428341。
full step 的 sampled metric 从 6.059037609450517e−10
变为 6.059037609454898e−10，虽只增加约 4.4e−22，仍无据称为下降；
因此**不采用下行补丁**，全图只加上面的上行 W。

较密的观察网格验证的是同一个候选，不是一列越来越细的实际新解；
它不能支付固定 g 的误差趋零。

## 4. 全域保守预算及尚待支付的几何预算

对已拟合的二进制系数，以 Fraction 作绝对值有理求和得到显示值

$$S_0=\sum_k(|c_{r,k}|+|c_{z,k}|)\approx2.616447023863865\cdot10^{-9},$$
$$S_1=\sum_k[(k+1)|c_{r,k}|+k|c_{z,k}|]\approx7.67381059306823\cdot10^{-8},$$
$$S_2=\sum_k[(k+1)^2|c_{r,k}|+k^2|c_{z,k}|]\approx2.3349066898412734\cdot10^{-6}.$$

用 \(\chi\le1/64\)、\(|\chi'|\le3/(16L)\)、
\(|\chi''|\le3/(2L^2)\)，有理比较给出

| 导数 | 整个支持的上界 |
|---|---:|
| \(|W|\) | 4.1e−11 |
| \(|W_s|\) | 3.84e−9 |
| \(|W_u|\) | 1.2e−9 |
| \(|W_{ss}|\) | 2.4e−7 |
| \(|W_{su}|\) | 1.13e−7 |
| \(|W_{uu}|\) | 3.65e−8 |

这些不等式只用有限精确二进制系数和三角函数绝对值 ≤1，
不需要密集网格覆盖。R112/R114 给原物理坐标 σ=s/λ，其中 λ<2，
且此支撑原目标半径至少 2/5，故

$$\|dW\|_{g\to\mathbb R^3}\le
\sqrt{4|W_s|^2+(25/4)|W_u|^2}<9\cdot10^{-9}.$$

设 R21 原图全域相对缺陷界为 d=2.57212e−8，则恒等式直接给

$$\|(X+W)^*e-g\|_{g,\mathrm{op}}
\le d+2\sqrt{1+d}\,(9\cdot10^{-9})+(9\cdot10^{-9})^2
<4.4\cdot10^{-8}.$$

这是守住 1e−6 预算的全域粗界；不是对原全域上确界的改善。
这里从头到尾是 **R21 的 X+W**，
不能将 R114 的 1.2566772507606437e−9 证书自动挪来。

reach 应继续用本题 R10 的已有定理，或 R4 的既有环境扰动定理。
目前可用的量是 R21 原 support>0.7370435198982138、
原前缀曲率<5.547266，实际全图曲率上界<8.462560 来自未动的尾部。
若对改变片补付足够松的实际 Cartesian 二 jets 界，
可将新前缀曲率保持在 6 以下并维持 support>0.736，
从而沿用未动尾部给出的全图曲率上界，直接应用 R10。
本文尚不把“这个余量很大”当作该二 jets 界已经计算完成。
同理，旧 δ_E 的非零证书也须检查它所用观察量是否在修改区之外，
不能因为 \(|W|\) 很小就无条件复制。

## 5. 复现、恢复身份与继续入口

成功运行的原命令为：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flexible-closed-surface/scripts/6a65-m12-weak-stress-screen.py \
  --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
  --out /tmp/visible-flex-6a65e705/exact-work/weak512g8-normal-fit.json \
  --angular 512 --gauss 8 --cartesian-correction

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flexible-closed-surface/scripts/6a65-m12-weak-stress-screen.py \
  --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
  --out /tmp/visible-flex-6a65e705/exact-work/weak1024g12-normal-actual.json \
  --angular 1024 --gauss 12 \
  --apply-correction /tmp/visible-flex-6a65e705/exact-work/weak512g8-normal-fit.json
~~~

2026-11-26 执行环境随后失联并被空环境替换；
上述临时数据和未提交的原脚本没有留在新文件系统。
因此旧源码 SHA 只标识已执行版本，
**不能把根据公式重写的脚本冒充为那个 SHA 对应的源码**。
恢复版另名 scripts/6a65-m12-weak-stress-recovered-v2.py；
其新实跑应另记源码哈希、参数十六进制值、输出哈希和与上表的差异。
本节如尚没有新 run ID，就仍是旧实跑的保全记录与恢复配方，
不是恢复版本已经重现全部旧数值的声明。

源输入可在 checkout 的对象可用时由
git cat-file blob 26ce0426c60ef868c53597a82252e0559c1cc21e
写入临时目录，必须校验上述 SHA256；也可用 GitHub blob API 将 content
base64 解码到 runner 临时目录。不要将可再生 NPZ、扫描 JSON
或 Actions 输出再提交进仓库或 Release。

下一实际闭环应扩大独立径向应力块与角频率，同时保留同一原 g，
每次求解后检查真实全 Gram，而不是继续增加同一候选的观察节点。
如改在 R114 背景上工作，应明确计算
\(((X+W)\circ\Phi)^*e-g\)，包括 W∘Φ 的真实导数；
只有加一个保守 sup 预算不能证明 R114 背景上的实际下降。

来源：R213 给本文弱应力恒等式和真实 Gram 变化；R21、R112、R114
给底图、原目标、桥坐标和既有有限证书。本节不引入外部存在性定理。


## 6. 恢复版已完成的新实跑（同日追加）

恢复源码另用 SHA256
fdf510d186d7fe7dfc9a9b7679838c811f20a69e31873c270cd9e7af4a1e724b，
并未复用旧源码身份。源 payload 已从原 Git blob 重新取得，完整 SHA256 相同。
恢复版逐字节对应仓库的
scripts/6a65-m12-weak-stress-recovered-v2.py，已通过语法编译检查并实际完成：

| 新 run | exit | 秒数 | 输出 SHA256 |
|---|---:|---:|---|
| up / 512×8 拟合 | 0 | 4.722198251998634 | 06fce726301a9820060527d27709aa8d25e7873a7b324cc38315e66e4a12f752 |
| 同一 up / 1024×12 实际复核 | 0 | 10.804413977995864 | 1227a05286731223ae812ee0091daab49d38a9575116855cf1b2eaf46ed81133 |

新拟合仍为秩 12，σ_min/σ_max = 0.29451728103840813；
其行归一线性残差最大值 8.271806125530277e−25。
新 1024×12 复核给

| 步长 | sampled metric 最大值 | 十二弱矩最大归一比 |
|---|---:|---:|
| 原图 | 1.0483379368590728e−9 | 2.2531697917975895e−12 |
| 1 | 1.04737437165717e−9 | 3.525020918175275e−20 |
| 1/2 | 1.0433651834934206e−9 | 1.1265848959546514e−12 |
| 1/4 | 1.0420482505245795e−9 | 1.6898773438761914e−12 |
| 1/8 | 1.0451930936890393e−9 | 1.9715235678369084e−12 |

新 sampled \(\|dW\|_F\) 最大值 7.440104475753376e−10。
数值与旧版非常接近，但表中保留各自真实输出，未宣称逐字节重现旧版。
恢复版也重新用 Fraction 核了 §4 六个导数上界、\(dW_g<9e-9\)
及全域 \(4.4e-8\) 粗界，全部为真。

当前采用候选由参数文件
notes/2026-11-26-6a65-m12-up-patch-parameters.json
中的 24 个 binary64 十六进制值准确冻结，前 12 个为径向系数，
后 12 个为竖直系数；两组都按 k=3,6,…,36 排列。
该文件只是小型定义参数，不包含可再生扫描输出。
其 hex 值应以 float.fromhex 解释，再作为精确二进制有理数定义 W；
这使候选不依赖以后重新拟合时的 BLAS 或末位舍入。

新命令与 §5 相同，但脚本换为 recovered-v2，
两次均加 --region up，并使用新的输出路径。
也可以将参数文件指定为 --apply-correction 输入：
它只保留求值器所需的固定系数与来源身份，实际复核不需要拟合 JSON 的其它数据。
新运行尚未做连续弱矩积分或新全域曲率扫描，
因此不把上表升级为连续证书或 G5 完成。

