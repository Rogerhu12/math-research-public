# 原 M12 前缀的真实总 Gram 连续消费者与 G12 完整第16单元

本条给出新的完整非线性相关 Gram 连续消费者，并实际消费原 Q-free G12
场的完整 W 第16单元：该单元正是旧 v4 预算的全域最坏前缀单元。
全单元、全角上界为

\[
\|g^{-1/2}(Y^*\delta-g)g^{-1/2}\|\le
\frac{9669347757025690801}{158456325028528675187087900672}
<6.102217\times10^{-11}<2\times10^{-9}.
\]

这是指定单元的严格连续结果，尚未覆盖其余前缀与全 tail。
没有据此宣称完成 README #5，也没有把节点峰值冒作连续界。
完整 proof、实际输入身份与自然退出记录如下。

## 1. 要包的确切对象

固定原数据 `m12-prefix-data.npz.gz`、原 common-cut 元数据、原 exact-root
bridge，固定一个真实保存的 Cartesian B-spline/Fourier 系数文件。
物理图定义为原参考 `Y=X+C+W`。`C` 是原 solver 已定义的中心二 jet
Hermite 匹配；没有加入 R250 的 `Q`，没有修改原目标 `g`，也没有重新求解。
令原 native 径向坐标为 `n`，物理弧长为 `q=n/lambda`，
`lambda=n_end/S`，完整半域单位坐标 `z=q/T`，`T=S+(.6-.15)`；所有小数参数
均按原 binary64 的精确 dyadic 值读入。`S` 的原 exact-root 区间始终保留。

目标为 `dq^2+f(q)^2 du^2`。直接形成的三个量是

\[
 E=|Y_q|^2-1,\qquad F=Y_q\cdot Y_u/f,\qquad G=|Y_u|^2/f^2-1.
\]

先把原 `X`、`C` 与完整 `W` 加在同一笛卡尔分量内，再点乘和减去原目标。
最终用 `max(|E|,|G|)+|F|` 包相对 Gram 的算子范数。这里没有添加旧统一
`d0` 或 `2|DX||D(C+W)|`；这些项本来就已经在同一个有符号总式中相消。
这延续了 R114 先形成相消量再取绝对值的原则，但本消费者是实际新的
笛卡尔有限场的完整非线性 Gram，而不是旧 Lie/线性物质修复的复述。

## 2. 原中央材料角的确切求值

原中心平面曲线写为 `gamma(theta)=sum gamma_k exp(i k theta)`，
系数是原数据的精确有理数；其频率为 `1 mod 3`，所以平方速度只含
`3j`。记

\[
 \rho_0=1-e_0\cos3\theta,\quad
 \Delta=|\gamma'|^2-\rho_0^2,\quad J=|\gamma'|,\quad
 a=(2\pi)^{-1}\int_0^{2\pi}J,
 \quad u(\theta)=a^{-1}\int_0^\theta J.
\]

`Delta` 在精确系数层相减。设 `rho_min=1-|e0|>0`，
`d=||Delta||_1`，`t=d/rho_min^2<1`。

\[
 J=\rho_0+\frac{\Delta}{2\rho_0}
       -\frac{\Delta^2}{8\rho_0^3}+R_b,
 \qquad |R_b|\le
 \rho_{\max}\frac{t^3}{16(1-t)}.
\]

这是 `sqrt(1+x)` 在二阶之后的绝对几何余项，因为从三阶起的二项式
系数绝对值均不超过 `1/16`。这里 `e0>0`。令
`s=sqrt(1-e0^2)`、`t0=e0/(1+s)`，则

\[
 \rho_0^{-1}=s^{-1}\sum_{k\in\mathbb Z}t_0^{|k|}e^{3ik\theta}.
\]

保留 `|k|<=64`，其尾项 `epsilon_R<=2 t0^65/(s(1-t0))`。两项代入上式后，
另付
`d*epsilon_R/2 + d^2*3*(||R64||_1+epsilon_R)^2*epsilon_R/8`。
所得偶实 Fourier 多项式 `P_J` 满足 `|J-P_J|<=epsilon_J`。
区间系数卷积本身每步向外，不把数值系数当成准确值。

若 `P_J=b0+sum_{k>=1}2 b_k cos(3k theta)`，则 `a` 位于
`b0 +/- epsilon_J`，并与原 R226 的已证 `a` 区间相交。归一化原始函数用

\[
 u(\theta)=\theta+
 \frac{\sum_{k\ge1}2b_k\sin(3k\theta)/(3k)}a+R_u,
 \qquad |R_u|\le 2\epsilon_J|\theta|/a_{\min}.
\]

这由把余函数的平均值和原始函数一起相减得到；不会把 mean radius
误差错误地当成独立的大相位项。丢弃的极小 Fourier primitive 项另外按
完整系数绝对和支付。这个 `u` 是原曲线的真实材料角。
高阶导数不对截断近似求导：直接使用准确有限 Fourier 的
`J=sqrt(rho0^2+Delta)` 与恒等式 `u'=J/a`。因而节点精确值的小统一余差
不会被错误放大为未知高阶导数。

## 3. 原 native 图和中心匹配项

原 native 坐标 `psi` 满足

\[
 u=\psi-e(n)\sin3\psi/3,\quad
 \rho=1-e(n)\cos3\psi>0,\quad
 \nu=-e_n(n)\sin3\psi/3.
\]

源 Hermite 的每个五次片由原数据和 `mean_increments` 精确有理重建。
其平均高度可以取片内零常数，因为这里只使用正径向或角导数。
在固定的原 source/chart 片内，完整物理一阶为

\[
 X_q=\lambda(X_n-\nu X_\psi/\rho),\qquad
 X_u=X_\psi/\rho.
\]

每个 cylindrical 分量都在同一 `psi` 下旋转回笛卡尔坐标。

中心 `psi0` 是相同 `u(theta)` 在 `e=e0` 时的真实逆角。
原 central second numerator `P` 在精确 Fourier 系数层形成：

\[
 P=\rho_0 X_{nn}+(e_{nn}(0)/3)\sin3\psi\,\gamma'(\psi).
\]

于是中心有符号差为

\[
 d_0=\gamma(\theta)/a-\gamma(\psi_0),\quad
 d_1=(1-\lambda)e_z,\quad
 d_2=-\lambda^2P(\psi_0)/\rho_0(\psi_0).
\]

所需材料角导数准确为

\[
 (d_0)_u=\gamma'(\theta)/J(\theta)
               -\gamma'(\psi_0)/\rho_0(\psi_0),\qquad
 (d_1)_u=0,
\]
\[
 (d_2)_u=-\lambda^2
 \frac{P'(\psi_0)\rho_0(\psi_0)-P(\psi_0)\rho_0'(\psi_0)}
      {\rho_0(\psi_0)^3}.
\]

在原 `h=Tu*eps` 支撑内，`C=sum H_j(q/h)d_j`，使用原三条物理五次
Hermite 多项式（含 `h` 与 `h^2/2` 因子）。所以
`C_q=sum H'_j(q/h)d_j/h`、`C_u=sum H_j(q/h)(d_j)_u`。
支撑外 `C=0`。这些是原参考的一阶，绝非另造参考后沿用旧身份。

保存的 `W` 通过原 R236 的准确 Boehm 插点提取为每片六个 Bernstein
控制行；转成等价五次幂基后，径向导数按真实 `T` 和片宽缩放。
笛卡尔平面部分保留完整 `1+3j` 正负频率，高度部分保留完整 `3j`
余弦频率。材料角导数是 `W_u=(a/J)W_theta`。

## 4. 区间实 Jet 和隐式角

区间算术采用运行环境 `numpy.longdouble` 的 IEEE 基本运算，每次以
`nextafter` 向外扩一端。精确有理数转换后还用整数比较修正端点。
平方根只用 libm 提供起点，最终每一端的平方用精确 dyadic 整数比验证；
三角函数通过 Machin 有理 `pi` 区间、象限约化与 49/48 次 Taylor 加完整
导数余项计算。没有把 unchecked `sin/cos/sqrt` 的返回当作严格端点。

实 Jet 存 `f^(j)/j!`，以标准乘法卷积、正分母倒数递推与平方根递推
包导数。隐式角的数值 Newton 只给提议 `p`；准确残差除以
`1-sup|e|` 包住真正根，故提议本身无证明地位。
设 `s=sin3psi`、`c=cos3psi`。第 `j` 阶先移除唯一含 `psi_j` 的项，写
`sin(3psi)_j=3 c0 psi_j+s*_j`，则

\[
 \psi_j=\frac{u_j+(e_0s^*_j+\sum_{k=1}^j e_k s_{j-k})/3}
                   {1-e_0c_0}.
\]

其中 `s*_j,c*_j` 由已知较低阶系数的三角微分递推得到。原分母严格正。
给定一个真实变量盒，每个 Jet 的第 `j` 项因而同时包含盒中每一点的
准确 `j` 阶导数除以阶乘，适合 Taylor 或插值余项。

## 5. 连续 tensor Chebyshev 余项

每个实际解析矩形在两方向仿射化到 `[-1,1]`。采用 `N` 个第一类
Chebyshev 根；节点、DCT 权重和总 Gram 值均向外包。
把完整三 Gram 的张量插值多项式形成以后才取系数绝对和，利用
`|T_k|<=1` 得全矩形多项式界，保留节点之间的相消。

对一变量，`prod_j(x-x_j)=2^(1-N)T_N(x)`，所以

\[
 \|f-I_Nf\|_\infty\le
 2^{1-N}\sup |f^{(N)}/N!|.
\]

这里右边是归一化真实变量的区间 Jet 第 `N` 项；真实盒半宽已作为
输入 Jet 的一阶系数计入。DCT 显式公式给一个足够的
`||I_N||<=2N-1`：常数系数的节点绝对权重和为 `1`，每个其余系数的和
不超过 `2`，再用 `|T_k|<=1`。

因此双变量完整余项取

\[
 \min\{e_r+(2N_r-1)e_\theta,\quad
       e_\theta+(2N_\theta-1)e_r\}.
\]

两个式子都是各自合法的 tensor telescoping 包界，取最小仍是合法
上界。这与“采样最大值加猜测”不同：连续盒的全部余项都由同一个
原 source 和真实 field 的区间高阶导数付清。

## 6. 分段和参数相关切点的完整覆盖

source 和 chart 分界按原准确 native knots 分。目标 ramp 和 central C
分界在物理 `q`，`W` 分界在 `z`，它们映到 native 坐标涉及同一个
尚以严格区间保存的 `lambda,S,T`。不能把某个浮点中值的切点当作真实
精确切点。

本消费者枚举所有实际 `source/chart/target/C/W` 分支组合。对每个组合，
把其真实交集放入准确的 native 外包区间；例如
`q in [ql,qr]` 的外包为 `[lambda_lo*ql,lambda_hi*qr]`，
`z in [zl,zr]` 的外包用单调的
`K=n_end*(S+.6-.15)/S` 给 `[zl*Klo,zr*Khi]`。
在外包区间上只包该分支的解析多项式延拓，结论只用于该分支的真实
交集。每个真实点属于至少一个被枚举的组合，所有端点由原 C2 连续性
或任一相邻分支准确值覆盖；不要求原分片函数跨 knot 有高阶导数。

由此，外包重叠既不漏点，也不会把一个错误分支的公式强施给另一个
分支。报告分别标注指定 W element 的完整覆盖、列出的局部 source
覆盖与未覆盖的全 prefix/surface。当前 prototype 还显式拒绝原
common-cut 校正与 chart cutoff 支撑，不能凭局部代码宣称覆盖它们。

## 7. 已实际完成的 G12 第16单元

实际场为 `m12-work/h2-c2-m48-g12-04r1/result.json.field.npz`，完整二重
Gauss 加密后的 Q-free 原源场；原 `g` 与所有保存系数原样消费。冻结源码
位于 `exact-work/complete-prefix16-kernel/`，三文件使用相对目录互相加载。
后续优化不得用修改后的文件 SHA 冒充本次已经加载执行的版本。

| 输入或实现 | SHA256 |
|---|---|
| 实际 prefix 完整总 Gram 入口 | `803f4e1bb3919c1183b6eca03abc4476c053a07b4b8e7e2ff955571b4db72a29` |
| 向外区间、隐式 Jet 与 tensor 核 | `1d0f04b1e5714b5b31bcbdb0c2c8e4bd84a23a7b62391e3a7d713a681c0eac04` |
| 原中心准确 arclength/phase | `a12b0951e0530c1e359c40f229c6471d306f1369ee3a38c92a780fc7a06e908d` |
| 原 prefix 数据 | `359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0` |
| 真实 G12 保存场 | `5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8` |
| 真实 G12 网格 | `94a48337aedccd79810e02928bbe920334440d14df1eb68435c7a252969c07f0` |
| 真实 G12 nonlinear result | `ec5a051715e9609c07082924c7872dd3eec0e183bdc660139f452108644b1e57` |
| 同场 R226 | `d72e798d220014dbb553c4a54e06cf478a5f3be5154eacf78f67d2ffec2212a2` |
| 原 common-cut 元数据 | `253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2` |
| 原 exact-root bridge | `1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa` |
| 本次完整单元报告 | `d24a2f4bfff3f21ee6c3dd81662ac5fb01ede5579cf971fc3ff80e8d33dc2550` |

运行输出 `exact-work/g12-prefix16-total-continuous.json`（172292 bytes）；
标准日志 `exact-work/g12-prefix16-total-continuous.log`。
实际自然退出码 0，完整运行 291.122856788 秒（含准确场提取与初始化）。

覆盖的原 source cells 为 353 到 379，共27个真实交集片。首尾 source
cell 只需要其与本 W 单元的交集；它们的整个原 cell 没有被误称成这个
单元的一部分。所有 source/chart/target/C/W 分支交集逐一支付；原根参数
相关切点使用第6节的准确外包与解析延拓覆盖。源在此尚未进入旧 common-cut
修正或 chart cutoff 支撑，中心 C 为原真实非零支。

W 第16单元的准确单位坐标端点为
`3315325741005983/36028797018963968` 与
`7367390535568851/72057594037927936`。
每个交集片用基本角域 `[0,pi/3]` 上128个闭区间盒；这是 D3 周期和
反射精确对称给出的完整角域，而不是只挑部分角度。每盒径向6、角向10
个 Chebyshev 根，所有两方向插值余项均由真实实 Jet 包住。

最坏交集为 source 363、原 chart 第7片、目标上坡第1解析片，
native 区间
`[8522531941082865/36028797018963968,
8558953017754161/36028797018963968]`，基本角盒86。
该片最终的完整矩阵上界正是本条开头的准确有理数。

下表是所有27片的分量连续预算摘要（display 只供读数，准确上界在 JSON）：

| 分量 | 全域分量上界 | 完整余项上界 | 径向余项上界 | 角向余项上界 |
|---|---:|---:|---:|---:|
| E | 2.8315310215e-11 | 3.701222725e-16 | 3.50067151192e-16 | 8.62856358209e-18 |
| F | 3.47099803283e-11 | 4.22095401044e-16 | 2.19720952157e-16 | 2.23001334825e-17 |
| G | 4.1083631476e-11 | 8.75219345961e-16 | 2.84373034089e-16 | 5.9303172539e-17 |

三个分量各自最大值不一定出现在同一个角盒；实际最终矩阵界按每一盒
`max(E_bound,G_bound)+F_bound` 形成后再取全域最大，未错把不同盒的相关性
当作同一盒。报告也保存节点区间宽度作为诊断，所有节点误差已进入 DCT
系数区间，不另外借节点高精度推导未经支付的连续界。

原中央辅助量本次实际精确消费得到：`epsilon_J` 不超过
`10487266613757502229/5575186299632655785383929568162090376495104`，
平均半径区间为
`[4611686018427361189/4611686018427387904,
18446744073709444767/18446744073709551616]`；primitive 保留70个非零模式，
所有被截断的模式与 binomial/inverse-series remainder 均明确入账。
该新相位消费者是本次关联计算的实际输入，不是把旧 `u0` 静默当成 `u`。

## 8. 推进范围

旧 v4 在此完整 W 单元以 source 全局误差与差分范数三角组合得到约
`9.96322e-7`，本条对同一个真实保存场直接包总 Gram 得到 `<6.102217e-11`。
这准确定位并清除了该单元的预算损失，说明原统一 `d0` 不是这张实际图
的真实误差下限。此处既没有更改物理图也没有采用新的 Newton 步。

完整前缀还必须把下坡、bridge、旧 common-cut 校正和 cutoff 支撑都接入
同一总式；完整曲面另须消费全 tail。两者实际完成前，本条不会升级为
全域 `B=2e-9`，不会升级为 G5 或 README 完成声明。

## 9. 实际命令与可移植入口

本次实际执行的完整命令为（工作目录 `/workspace/scratch/2ecfcd6930d6`）：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python exact-work/m12-prefix-total-gram-local.py \
  --scripts math-research-public/topics/visible-flexible-closed-surface/scripts \
  --data m12-work/m12-prefix-data.npz.gz \
  --field m12-work/h2-c2-m48-g12-04r1/result.json.field.npz \
  --grid m12-work/h2-c2-m48-g12-04/grid.json \
  --result m12-work/h2-c2-m48-g12-04r1/result.json \
  --correction-bounds m12-work/h2-c2-m48-g12-04r1/correction-bounds.json \
  --complete-element --element 16 --angular 128 --nr 6 --na 10 --batch 8 \
  --out exact-work/g12-prefix16-total-continuous.json \
  > exact-work/g12-prefix16-total-continuous.log 2>&1
```

`--radial-subdivisions` 实际使用默认值 `1`；没有省略一个实际采用的额外
细分参数。`--complete-element` 触发枚举所有实际交集；没有同时传局部
`--source-cells`。`--angular 128` 指基本域 `[0,pi/3]` 的128个盒。

三个冻结脚本的 basename 分别是：

- `m12-prefix-total-gram-local.py`：CLI 入口；
- `m12-correlated-gram-interval-kernel.py`：区间、Jet 和 tensor 核；
- `m12-original-central-arclength-interval.py`：原中心相位及有符号 trace。

三者必须放在同一目录，以保相对加载和本条所列内容 SHA。发布到 topic
的 `scripts/` 后，只需把上述 Python 入口改为
`math-research-public/topics/visible-flexible-closed-surface/scripts/m12-prefix-total-gram-local.py`；
其余输入位置可由操作者提供，内容须匹配第7节 SHA。原 `--scripts` 参数
仍指向包含原 R226/R236 与 source/chart 供应器的 topic scripts 目录。
输出路径必须尚未存在，消费者不会覆盖旧完成回执。
