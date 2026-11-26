# R220：原 M12 同一 g 的非圆精确 affine 参考与全周期 Green 域

2026-11-26，Astra-visible-flex-6a65e705/g5_and_exact。

**状态：下述精确环带、全角度及全径向定义域、曲率和 R218 的定量法向 Green 常数已证明并实际完成有理区间核算。**
原 M12 邻段的完整空间端迹尚未匹配；没有构成新的闭曲面或完成 README 第 5 条。
本结论消费 R137 的现有直纹公式，不把近似 M12 的 II 当成准确 Gauss–Codazzi 数据。

## 1. 原固定度量与新的精确参考

原 M12 对象是 R21 的第一档 critical 闭图。元数据
`../notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json`
的 SHA256 为
`253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2`。
其二进源数据的 SHA256 为
`359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0`。
公共 cut 修正在本节入口之前恒为零；本次入口落在原源数据的第 504 个 Hermite 单元。

记上升斜率、ramp 比例及幅度为元数据中的精确二进有理数

$$v=.17,\quad \epsilon=.4,\quad \delta=.07254443456654512,$$

并定义

$$T_u=\frac{\delta}{v(1-\epsilon)},\qquad
c_0=1-\frac{\delta\epsilon}{2(1-\epsilon)}.$$

原物理旋转度量在相应 affine 段上准确为

$$g=d\sigma^2+(c_0+v\sigma)^2du^2.                 \tag{1}$$

这里没有以求积所得的入口周长重新定义 $g$。
R21 使用的 native 坐标与物理坐标关系为 $s=\lambda\sigma$，
$\lambda$ 是原精确 bridge 的唯一根所确定的旧总长/精确总长比值。
它已有 `2026-11-09-db6f-root-exact-bridge-m12.json` 中的严格有理区间；
该文件 SHA256 为
`1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa`。
本结论使用同一个 $\lambda$，并没有把显示值 $1.0000000000000004$ 当成定义。

取以下两个精确 native 有理数：

$$
s_a=\frac{12869634856555301714754456594821}{44134523297546036379737891607500},
\quad
s_b=\frac{18519718452116164352243510990459}{44134523297546036379737891607500}.
$$

它们是 $T_u[\epsilon+(1-2\epsilon)/20]$ 与
$T_u[\epsilon+19(1-2\epsilon)/20]$。
设

$$\sigma_a=s_a/\lambda,\quad L=(s_b-s_a)/\lambda,
\quad f_0=c_0+v\sigma_a.                          \tag{2}$$

整个 $[\sigma_a,\sigma_a+L]$ 严格位于原 affine 段内部。
显示值为 $\sigma_a\simeq.29160017815964207$、
$L\simeq.12801959041155014$、$f_0\simeq1.0253905520982909$。
以下使用平移后的物理坐标 $x=\sigma-\sigma_a\in[0,L]$，
故目标准确为 $dx^2+(f_0+vx)^2du^2$。

### 1.1 原源曲线的精确有理定义

在 $s=s_a$，按照保存的二进有理节点、零至二阶 jet 作准确五次 Hermite 插值。
平均高度的节点值是保存增量的**准确有理累加**，不使用舍入后的累计高度之差。
于是得到有限柱坐标 Fourier 曲线

$$\gamma(\psi)=R(\psi)e_r(\psi)+T(\psi)e_\theta(\psi)+Z(\psi)e_z,$$

$$R=r_0+\sum_{j=1}^{24}r_j\cos3j\psi,\quad
T=\sum_{j=1}^{24}t_j\sin3j\psi,\quad
Z=z_0+\sum_{j=1}^{24}z_j\cos3j\psi,                \tag{3}$$

所有系数为明确有理数。转换到 Cartesian Fourier 用恒等式

$$X+iY=(R+iT)e^{i\psi},$$

其中 $R+iT$ 在频率 $\pm3j$ 的系数分别为
$(r_j+t_j)/2$、$(r_j-t_j)/2$。
所以最高 Cartesian 频率为 73；没有 DFT，也没有丢弃某个尾模。

记

$$J=|\gamma_\psi|,\quad
a_\gamma=\frac1{2\pi}\int_0^{2\pi}J(\psi)\,d\psi,\quad
u(\psi)=\frac1{a_\gamma}\int_0^\psi J(t)\,dt.$$

下面的区间证明给 $J>0$，因此 $u$ 是圆周的准确次数一微分同胚。
令 $C=(0,0,z_0)$，定义新入口

$$\widehat\gamma(u)=C+\frac{f_0}{a_\gamma}
       \bigl(\gamma(\psi(u))-C\bigr).              \tag{4}$$

这里 $a_\gamma$ 是上述**精确积分**。
因此 $|\widehat\gamma_u|=f_0$ 是恒等式；较宽或较窄的积分包围
只影响证书，不改变几何、度量或归一参数。
实际数值供应器用求积近似 (4)，其舍入误差不参与下文的有理证明。

原系数的三重对称和反射关系由 (3) 准确保留。
程序还准确核算了原高度差
$\gamma_z(0)-\gamma_z(\pi/3)=2\sum_{j\ {
m odd}}z_j>0$；
归一后的差严格大于 $.0046$。所以这个入口并非绕指定 $z$ 轴的水平圆，
没有退回旋转面的圆截面参考。更一般地，若它是一个空间圆，三重旋转对称将保持该圆的唯一平面；非平凡的三分之一周绕轴旋转所保持的平面只能是水平面，矛盾。

## 2. 从同一曲线构造全部相容入口数据

令 $T=\gamma_\psi/J$，$\mathsf N,\mathsf B$ 为原曲线的 Frenet 法向和副法向，
$\kappa,\tau$ 为其曲率和挠率。写

$$b=|T_u|=a_\gamma\kappa,\quad r=v/b,\quad
c=\sqrt{1-r^2},$$

$$d=-r\mathsf N+c\mathsf B,\qquad
N=d\times T=c\mathsf N+r\mathsf B.                \tag{5}$$

全角区间证明给 $b>.6111>v$，故 (5) 是完整圆周上的光滑正分支。
设置

$$n=\frac{cb}{f_0}>0,\qquad
m=\frac{-a_\gamma\tau-r_u/c}{f_0},\qquad k=m/n.   \tag{6}$$

从 Frenet 公式直接得到

$$\widehat\gamma_u=f_0T,\quad
d_u=vT+f_0mN,\quad T_u=-vd+f_0nN,\quad
N_u=-f_0md-f_0nT.                                \tag{7}$$

例如 $d_u$ 的 $T$ 分量是 $rb=v$；其 $N$ 分量为
$-a_\gamma\tau-r_u/c$。
因此 (7) 是由同一真实曲线推出来的结构方程，而非分别拟合后的近似标架。
对这些恒等式求导，得到 R137 需要的完整位置、标架、$m,n$ 的角向两 jet。

对于证明所需的 $k_u$，可以只使用原曲线至四阶导数。记

$$p=\gamma',\ q=\gamma'',\ r_3=\gamma''',\ s_4=\gamma'''',
\quad E=p\cdot p,\ C_1=p\times q,\ H=C_1\cdot C_1,$$

$$A=C_1\cdot(p\times r_3),\quad B_1=p\cdot q,
\quad \kappa=\frac{\sqrt H}{E^{3/2}},\quad
\tau=\frac{C_1\cdot r_3}{H}.$$

则

$$h=\frac AH-3\frac{B_1}E=\kappa'/\kappa,$$

$$h'=\frac{|p\times r_3|^2+C_1\cdot(q\times r_3+p\times s_4)}H
-\frac{2A^2}{H^2}-3\frac{|q|^2+p\cdot r_3}E+6\frac{B_1^2}{E^2},$$

$$\kappa'=\kappa h,\quad \kappa''=\kappa(h^2+h'),
\quad \tau'=\frac{C_1\cdot s_4}H-2\tau\frac AH.    \tag{8}$$

这里撇号均指原角 $\psi$。
由 $\partial_u=(a_\gamma/J)\partial_\psi$ 和 (6)，

$$k=-\frac{a_\gamma\tau}{cb}
       +\frac{v b_u}{c^2b^3}.                    \tag{9}$$

对 (9) 按 $\psi$ 求导，再乘 $a_\gamma/J$，正是证书脚本的 $k_u$。
(8)–(9) 保留全部非旋转系数，没有使用逐 Fourier 模解耦近似。

## 3. 精确 R137 环带、完整周期与尺度

引用 R137 已证明的构造，置 $r_0=f_0/v$，

$$\Delta=x(2r_0+x),\qquad
w=\frac{\Delta}{r_0+\sqrt{r_0^2+(1+k^2)\Delta}},$$

$$Y=\widehat\gamma(t)+w\,[d(t)-k(t)T(t)],\qquad
U=t-\frac1v\arctan\frac{kw}{r_0+w}.              \tag{10}$$

这里 $t$ 是入口材料角，$U$ 是当前材料角。分母 $r_0+w>0$，
所以选取的 arctan 分支在整个定义域光滑、周期。
又有

$$D=f_0+w\,[v(1+k^2)-k_u],\qquad
U_t=\frac{D}{v[r_0+(1+k^2)w]}.                  \tag{11}$$

第 4 节证明 $D>.8288$、$U_t>.7893$。
因为所有入口数据 $2\pi$ 周期，(10) 满足
$U(t+2\pi)=U(t)+2\pi$；严格正导数与次数一共同给完整圆周上的全局微分同胚。
所以可以在每个 $x\in[0,L]$ 唯一反解 $t=t(x,U)$，
没有缺失回程扇区，也没有只在一条局部角弧上定义解。

(7) 和 R137 于是给

$$Y^*e=dx^2+(f_0+vx)^2dU^2                       \tag{12}$$

**准确成立**，并给完整 Cartesian 两阶端迹。
本参考在闭环带上为光滑浸入；不以有限网格上的 $10^{-15}$ 残差证明 (12)。

原 bridge 的 $\lambda$ 只通过 (2) 决定物理入口、长度和固定半径。
(5)–(12) 的径向变量就是物理弧长 $x$，$n$ 中分母为物理 $f_0$。
下面的主曲率是该真实空间图的物理主曲率，**不需要再乘一个 $\lambda$**。
与旧 M12 端迹作比较时，旧图的 native 一阶、二阶径向导数则分别乘
$\lambda$、$\lambda^2$，混合导数乘 $\lambda$；实际 adapter 已这样做。

## 4. 全圆周与全径向区间证书

`../scripts/6a65-m12-r137-continuous-domain.py` 中所有决定界的运算为
96 位 dyadic 区间的整数向外舍入。加、减、乘、除逐次向外舍入；
平方根下端为整数平方根，上端向上补一。
输入有理数和 bridge 区间先准确转为 dyadic 包围。

### 4.1 三角函数与整段 Fourier 导数

$\pi$ 用 Machin 公式及 $\arctan(1/5),\arctan(1/239)$ 的 80 项
交错级数和下一项界包围。
将全圆周分成 $N=8192$ 个等角区间，半宽 $\eta=\pi/N$。
每个中心上的 $m\psi$ 都按准确有理倍 $\pi$ 约到 $[-\pi,\pi]$。
sin 用至 49 次、cos 用至 48 次 Taylor 多项式；余项分别不超过
$4^{50}/50!$、$4^{49}/49!$。

对每个 Cartesian 分量、每阶 $0\le j\le4$，中心导数再加

$$\eta\sum_{m=1}^{73}m^{j+1}(|a_m|+|b_m|)        \tag{13}$$

作为整个角区间的绝对误差。
这是有限 Fourier 导数的直接 Lipschitz 界；并非把中心点采样当作整格值。
由此得到每格 $\gamma,\gamma',\ldots,\gamma''''$ 的包围。

### 4.2 精确弧长积分余项

整圈严格得到 $J>.3927237180$。
由

$$J''=\frac{|\gamma''|^2-(\gamma'\cdot\gamma'')^2/J^2}{J}
       +\frac{\gamma'\cdot\gamma'''}J$$

可用

$$|J''|\le\frac{\|\gamma''\|_\infty^2}{\min J}
               +\|\gamma'''\|_\infty<19.453574.$$

因此 $a_\gamma$ 的复合 midpoint 平均误差不超过

$$\frac{\eta^2}{6}\,19.453574 < 4.768349\cdot10^{-7}.\tag{14}$$

中心求值本身也已作区间包围。准确积分最终满足

$$1.0253900752634134<a_\gamma<1.0253910289331521.  \tag{15}$$

数值 Gauss 求积约为 $1.0253905520982827$，只作为额外观察。
(15) 虽比该显示值宽，却已经足够证明全部定义域余量。

### 4.3 全径向区间，不只两端

对每个原角区间，用 (8)–(9) 区间运算得到 $b,n,k,k_u$。
由 (10) 的正根方程

$$2r_0w+(1+k^2)w^2=2r_0x+x^2$$

立即得 $0\le w\le x\le L$。
证书把整段 $w\in[0,L]$ 代入 (11)，所以以下界覆盖整段所有点。
唯一非零主曲率准确为

$$\Lambda=\frac{f_0n(1+k^2)}D>0.                 \tag{16}$$

同一直纹上的 $N$ 恒定、直纹方向垂直于 $N$，故径向支撑
$-Y\cdot N=-\widehat\gamma\cdot N$ 沿直纹不变。
将 (5) 和 (4) 代入区间向量运算得到支撑界。

全部 8192 个角区间实际通过，向安全一侧取简洁有理数得到：

| 全域量 | 严格界 |
|---|---:|
| $|T_u|$ | $>.6111$ |
| 入口 $n$ | $>.5725$ |
| $|k|$ | $<.429876$ |
| $D$ | $>.8288$ |
| $U_t$ | $>.7893$ |
| 非零主曲率 $\Lambda$ | $.5725<\Lambda<2.6961$ |
| 外向径向支撑 $-Y\cdot N$ | $>.8036$ |

另一个主曲率准确为零。
这是开放环带的实际曲率和正支撑结论；没有套用仅对完整闭球面成立的 R10
而宣称本环带已经有全闭图 reach 证书。

## 5. R218 在此实际参考上的定量范围

每条直纹的物理弧长为 $w\sqrt{1+k^2}$，所以完整两端口的最大直纹长度满足

$$L_*<.139347.$$

第 4 节给实际 $|\operatorname{tr}_gII|>\lambda_*=.5725$；
这里 $\lambda_*$ 是主曲率下界，不是第 1 节的坐标比 $\lambda$。
入口、出口都是完整材料圆周；(11) 已证明所有直纹跨越域的全局坐标条件。
因而可以对这张**准确**参考使用 R218：

$$\mathcal C_g(B)=\tfrac12(\operatorname{div}\operatorname{div}B-
                            \Delta\operatorname{tr}B),$$

$$\operatorname{cof}II:\nabla^2w=-\mathcal C_g(B),\qquad
w(0,\theta)=\partial_\tau w(0,\theta)=0.$$

使用证书的未舍粗端点，完整零入口 Green 解满足

$$\|w\|_\infty<.016959\|\mathcal C_g(B)\|_\infty,$$

$$\|\partial_\tau w\|_\infty<.243395\|\mathcal C_g(B)\|_\infty,
\qquad
\|\partial_\tau^2w\|_\infty<1.746677\|\mathcal C_g(B)\|_\infty.\tag{17}$$

两端都固定还必须满足 R218 的**两整个周期函数**条件

$$\int_0^{L(\theta)}F(\tau,\theta)\,d\tau=0,
\qquad \int_0^{L(\theta)}[L(\theta)-\tau]F(\tau,\theta)\,d\tau=0,$$

其中 $F=-\mathcal C_g(B)/\Lambda$ 沿实际直纹取值。
开放领上源为零才可推出修正也在开放领上为零。
这两个 normal range 条件没有消去切向 annulus holonomy、完整切向端迹条件，
也没有提供横向 $C^2$ 的无损逆；R218 中的各项限制原样保留。

## 6. 与旧 M12 的完整端口：实际观察与未付账项

数值 adapter 采用同一精确曲线的浮点近似、256 个积分 panel、每 panel
24 点 Gauss、1024 个完整材料角节点，实际调用 R137 的全圆周反解。
入口与出口的真实 Gram 采样误差分别约为
$8.97\cdot10^{-16}$ 和 $1.12\cdot10^{-15}$。
精确等距来自 (12)，不是这两个小数。

按同一原材料角、同一物理径向坐标比较，新参考与旧 M12 的差为：

| 端迹 | 左端最大差（采样） | 右端最大差（采样） |
|---|---:|---:|
| $X$ | 9.4666521e-12 | 6.2436269e-10 |
| $X_\sigma$ | 4.9131349e-9 | 9.3978707e-9 |
| $X_u$ | 4.1629787e-10 | 4.0104239e-8 |
| $X_{\sigma\sigma}$ | 5.6610253e-7 | 3.6921160e-7 |
| $X_{\sigma u}$ | 3.6210348e-7 | 6.3622823e-7 |
| $X_{uu}$ | 4.1264068e-8 | 2.7915846e-6 |

这张表没有外向舍入，是实际构造的边界缺口观察；不能把非零端迹差改称已经拼接。
固定 Phi 的材料修正、端口空间匹配和非 affine 邻段求解也没有由本节自动完成。
原冻结 $f$ 在 affine plateau 外具有 $f''\ne0$ 的开 ramp，
故不能原样继续用 K=0 的 R137 公式穿过这些连接段。

精确参考也可生成
$Y_\alpha(x,u)=R_\alpha Y(x,u-\alpha)$；所有相位保持 (12) 和第 4 节的界。
但在完整闭图端口尚未对接之前，这仅是精确环带族，不能继承原闭图的固定帽、
held、非平凡性或 reach 结论。

## 7. 可复现命令与实际运行身份

需提交的两个新脚本为
`../scripts/6a65-m12-r137-fixed-metric-adapter.py` 和
`../scripts/6a65-m12-r137-continuous-domain.py`。
它们复用 `6a65-geometry-r137-exact-inlet-consumer.py` 和已登记的
`fd2d_k0_ruling_coast.py`；后两者 SHA256 分别为
`eaaa4ebe16aaea435b6fab6299018753d43ef91bbc28779e7375810e7dd252cd` 与
`2c28fe83b39992dc86208f08cfcb5e5469c391f3c725479e2ba0198bf8140d5c`。

adapter SHA256：
`5dbc39bcb44c88739bc089c1b3ebc4e3d07532c18d37737d2a72d7e96b384a78`。
连续证书源码 SHA256：
`6bc46eeeb91bb979c19c2167250ced2a8362ae92b8f8b53eacd8595408e2af57`。

从仓库根运行，输出留在 scratch，不提交可再生数组或扫描 JSON：

```bash
mkdir -p /tmp/visible-flex-6a65e705/exact-work
git cat-file blob 26ce0426c60ef868c53597a82252e0559c1cc21e > /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/visible-flexible-closed-surface/scripts/6a65-m12-r137-fixed-metric-adapter.py \
  --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
  --out /tmp/visible-flex-6a65e705/exact-work/m12-r137-up-1024p256g24.json \
  --angles 1024 --panels 256 --gauss 24

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/visible-flexible-closed-surface/scripts/6a65-m12-r137-continuous-domain.py \
  --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
  --out /tmp/visible-flex-6a65e705/exact-work/m12-r137-continuous-8192-final.json \
  --cells 8192
```

输出路径须是尚不存在的新路径。源数据长度 3,112,330 字节，SHA 已在第 1 节绑定。
数值 adapter 实际 exit 0，耗时 1.966159231000347 秒；报告 SHA256
`1f85048d13c49376b8b898424d5e1b567c64344bce6a1d2543ee3d6220222691`。
有理连续域证书最终实际 exit 0，耗时 37.19851770000241 秒；报告 SHA256
`22049752598fdad0435b836212099eea57863c783c6e5b9550e5e10441f14648`。
所有角区间的有序整数端点行流 SHA256 为
`8907f65751f3de718072cb8d0efd82f43355384c397c6efbb81f516a9c576e8b`。
该行流 hash 不含耗时，区间计算是确定的；报告含实际耗时，完整文件 hash 只绑定这次 receipt。

初次 1024 个角区间因区间宽度未能证明正 $D$，程序明确失败退出；
8192 个区间的改动仅细化对**同一个精确参考**的区间包围，未改变入口、
目标度量、曲线频数或相位范围。这是证书细化，不能把它冒称为 README 第 5 条的
全闭图求解加密序列。
