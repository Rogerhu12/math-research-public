# R131 续篇：同一十分之一真解的完整嵌入与曲率

2026-11-13，visible-exact-astra-ac0d。

**已证明并执行全部145个闭盒。** 原同一目标、同一原腰初值的真实
Codazzi 分支在
\[
[-1/10,1/10]\times\mathbb S^1
\]
上是精确 \(C^2\) 嵌入，统一覆盖原全部
\(\eta\in[-10^{-9},10^{-9}]\)。完整连续曲面满足
\[
\phi_\theta>0.21732971181,\qquad
J=z_r\phi_\theta-z_\theta\phi_r>0.20397941419,
\qquad |\kappa_1|,|\kappa_2|<10.480590.
\]
本篇将已证明的同一 \([0,.1]\) Cauchy 分支升级为实际嵌入环带。
它不是闭面、完整正帽/无限尾接合、共同度量可见弯曲族或最终 reach
的结论。不同辅助参数仍可能对应不同目标度量。

## 1. 只使用原分支和已付的真实误差

[完整三阶 native 与十分之一延拓](R131-supplement-complete-cubic-native-and-one-tenth-continuation.md)
已经证明同一原目标
\[
g_0=E(r)\,dr^2+a(r)^2\,d\theta^2,\qquad
\delta_*=-7789843107295549/4611686018427387904
\]
的真实解存在。\(E\) 仍是原真实候选 \(|F_r|^2\) 的完整角平均，
包括原无限 primitive 余项。原完整1024角有限 BC 候选及其全部
七次径向多项式保持不变；它只用作误差中心。

设
\[
k=\sqrt{-K},\quad P=(\widehat B+k)/\widehat C,
\quad Q=(\widehat B-k)/\widehat C.
\]
这里的 \(k\) 是真实目标系数，不是有限候选另算的曲率。
原145行严格 C0 屏障给每个闭盒上的
\[
\max(\|p-P\|_\infty,\|q-Q\|_\infty)\le e_i,
\quad q-p\ge d_i>0,\quad |p|,|q|\le M_i.
\]
本次先从原完整 native 独立重跑这个屏障，全部 JSON 数学字段与原
已通过证书逐项相同；随后才使用每行的 \(e_i,d_i,M_i\)。没有另设
更小的误差、初值或参数宽度。

## 2. 完整闭角符号门

新脚本从全部 byte shards 无损恢复完整有限候选，逐项核对原始
压缩字节 SHA、全部数组、准确共享端点和原对象身份。每个原径向盒
上仍按准确七次多项式进行有向区间 Horner；完整有限 Fourier 多项式
用4096个闭角 cells 包围。每个 cell 包括局部一、二阶 Taylor 项和
完整有限三阶导数余项，全部有限模式和 mean 都保留。

真实变量的闭包围准确取
\[
p\in P+[-e_i,e_i],\qquad q\in Q+[-e_i,e_i].
\]
145行、全角度和整个真实参数盒全部严格通过
\[
\boxed{-p>0.03148348137,\qquad q>0.03148348137.}
\tag{G.1}
\]
这是真实解的符号断言；没有用有限候选的符号直接替代实际解。
新的角网格只是给同一个有限函数的又一完整闭包围。原真实误差、
真实目标余项和全部 primitive 尾继续来自原完整证书。

## 3. 不通过小 gap 放大的标架系数

在 (G.1) 下置 \(x=-p>0,y=q>0\)。R126 的准确反变换给
\[
C=-\frac{2k}{x+y},\qquad
A=\frac{2kxy}{x+y}>0,\qquad
B=k\frac{x-y}{x+y}.
\]
因为 \(x,y\le M_i\)，逐点有
\[
|A|\le kM_i,\qquad |B|\le k,\qquad
|C|\le\frac{2k}{d_i}.
\tag{G.2}
\]
其中第一式使用 \(2xy/(x+y)\le\max(x,y)\)，第二式使用
\(|x-y|\le x+y\)。每个闭盒分别消费它自己的真实 \(k,M_i,d_i\)
界，再积分，未把不同盒的有利端点混用。

正交切标架中的第二基本形式是
\(\begin{pmatrix}A&B\\B&C\end{pmatrix}\)。由其对称性，
\[
\max(|\kappa_1|,|\kappa_2|)
\le\max(|A|,|C|)+|B|.
\]
在全部145个闭盒上取最大得到
\[
\boxed{\max(|\kappa_1|,|\kappa_2|)<10.480590.}
\tag{G.3}
\]
本式没有把局部曲率界改称闭面的全局 reach。

## 4. 从同一真实腰帧连续积分

R126 的真实重建满足
\[
F_r=\sqrt E X,\quad F_\theta=aY,\quad n=Y\times X,
\]
\[
X_r=\sqrt E A n,\quad Y_r=\sqrt E B n,
\quad n_r=-\sqrt E(AX+BY).
\]
原初始数据为 \(X(0)=e_z\)，\(F_0,Y_0,n_0\) 均水平。
原完整腰曲线的统一已证界仍为
\[
F_0\cdot n_0>1/2,\qquad |F_0|<13/10.
\tag{G.4}
\]

令单调积累上界
\[
\mathcal X(r)=\int_0^r\sqrt E\,|A|\,dt,\qquad
\mathcal Y(r)=\int_0^r\sqrt E\,|B|\,dt.
\]
它们从同一个真实腰帧开始，绝不在闭盒交界处重置。
正交性给
\[
|X-e_z|\le\mathcal X,\quad |Y-Y_0|\le\mathcal Y,
\quad |X_h|\le\min(1,\mathcal X),
\quad X_z\ge1-\mathcal X^2/2.
\]
因此水平位移满足
\[
|F_h-F_0|\le\mathcal H(r):=
\int_0^r\sqrt E\min(1,\mathcal X)\,dt.
\]
实际执行时在长度 \(h_i\) 的盒内使用
\[
\Delta\mathcal H\le
\min\{h_i e_i^*,\ h_i e_i^*\mathcal X_{i-1}
                  +h_i^2(e_i^*)^2 A_i^*/2\},
\]
其中 \(e_i^*\) 是该盒 \(\sqrt E\) 的上界，与前节误差 \(e_i\)
是不同的量。此式先积分该盒线性增长的 \(\mathcal X\)，不取一个
没有支付盒内变化的中点值。

由 \(n_h'=-\sqrt E(AX_h+BY_h)\)、\(|Y_h|\le1\)，还得到
\[
|n_h-n_0|\le\mathcal X^2/2+\mathcal Y.
\tag{G.5}
\]
全部有向算术的累积结果为

| 同一完整真实环带上的量 | 统一界 |
|---|---:|
| \(\mathcal X\) | \(<.288410795627\) |
| \(\mathcal Y\) | \(<.100610240649\) |
| 水平位移 \(\mathcal H\) | \(<.016670177207\) |
| 水平法向变化 \(\mathcal X^2/2+\mathcal Y\) | \(<.142200634166\) |
| 水平半径下界 | \(>.483329822792\) |
| 水平半径上界 | \(<1.316670177208\) |
| \(\det_h(F_h,Y_h)\) | \(>.352536509950\) |
| \(F_h\cdot n_h\) | \(>.298468998378\) |
| \(X_z\) | \(>.958409606481\) |

表中后五行直接由 (G.4)、\(|Y_h|,|n_h|\le1\) 及已积分的误差推出。
例如行列式下界为
\(1/2-\mathcal H-(13/10)\mathcal Y\)，法向支撑下界为
\(1/2-\mathcal H-(13/10)(\mathcal Y+\mathcal X^2/2)\)。

## 5. 完整圆周和整个环带的单射

正水平半径使 \(\phi=\arg F_h\) 在整个环带上有圆值定义。
准确恒等式为
\[
\phi_\theta=\frac{a\det_h(F_h,Y_h)}{|F_h|^2},\qquad
J=\frac{\sqrt E a}{|F_h|^2}\,F_h\cdot n_h.
\]
本次消费各盒真实 \(a,\sqrt E\) 的统一下界和完整水平半径上界，
严格得到开头的两个正下界。所有分母均在此前已证明非零。

原腰圆周的角映射次数为1；无水平零点的径向同伦保持次数。
因此每个固定 \(r\) 的 \(\theta\mapsto\phi\) 是一次定向微分同胚。
换成全局坐标 \((r,\phi)\) 后，
\[
\partial_r z\big|_\phi=J/\phi_\theta>0.
\]
若两个点的三维像相同，柱角与高度都相同，后式先迫使径向标签相同，
再由圆周单射迫使角标签相同。

R125/R126 的真实平面反射给负半带和腰接缝的 \(C^2\) 正则性；
水平半径、行列式、水平法向支撑和上述正 Jacobian 的界保持不变。
故该单射证明适用于整个 \([-.1,.1]\) 环带。已知精确度量使它是
\(C^2\) 浸入，紧环带上的连续单射又是到其像的同胚，从而是完整
\(C^2\) 嵌入，包括边界和腰接缝。

## 6. 完整产物和复核

新 producer 为 `scripts/fourfold_codazzi_cubic_sign_geometry.py`，
完整报告为 `notes/2026-11-13-R131-cubic-sign-r01-geometry-native.json.gz`。
报告保存全部145行真实符号包围、原完整径向盒、实际 germ、逐行真
误差、间隔、标架系数、连续积累量，以及所有输入和依赖 SHA。
`complete=true`、`embedding_certified=true`；没有只保通过行。

重现时指定新路径：

~~~sh
python scripts/fourfold_codazzi_cubic_sign_geometry.py \
  --out /tmp/cubic-sign-r01-geometry-reproduced.json.gz
~~~

newton_source 已独立验证 (G.2)、单调标架积分、(G.5) 及柱坐标
单射所需的正门，并完整重跑全部145行 native；只排除运行秒数后，
全部 JSON 字段逐值相同。其完整审计为
`notes/2026-11-13-R131-cubic-sign-r01-independent-newton-review.json`。
更外侧的跨根、非线性帽和无限平尾/mean/regular
匹配仍须继续；本结论不缩减最终共同度量闭面族的任何完成标准。
