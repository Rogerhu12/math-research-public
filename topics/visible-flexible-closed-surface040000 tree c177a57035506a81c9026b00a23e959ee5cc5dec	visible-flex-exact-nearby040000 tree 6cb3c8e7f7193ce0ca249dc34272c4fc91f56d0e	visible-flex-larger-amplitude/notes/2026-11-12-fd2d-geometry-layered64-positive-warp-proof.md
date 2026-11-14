# 两个固定分层 R64 尾的准确正伸缩

这份证明补上 2026-11-12-fd2d-geometry-layered64-slope-path-budget.md
中尚未支付的“准确 \(\lambda>0\)”前提。它针对 wc01 与 wc03 两个分别冻结
的物理度量；不把有限二进制校准残差解释成准确的 \(T_{21}=0\)，也不宣称
其非圆同度量解已经存在。

## 1. 固定定义

配置及 SHA256：

| 输入 | SHA256 |
|---|---|
| 2026-11-12-fd2d-layered64-wc01-recovery02-config.json | d4d41047c5afa1df90e17e3814e896a7cd91f64c79d0e11116e071cb97e17994 |
| 2026-11-12-fd2d-layered64-wc03-01-config.json | f0188f4e16ebbf69d237311d378b05cd860c130f0503fa7461b2fb3080f2df68 |

fd2d-layered-tail-scalar-packet.mjs 导出的 scalar packet 另给出原 source
前160格的全部 \(\alpha_n\)。以下前160格的 \(\alpha_n,\beta_n\) 以及两峰/
谷 cap level 解释为所列 binary64 的准确有理值。原几何常数
\[
 \delta_0=3/500,\quad c_0=1/20,\quad a=11/4,\quad
 r_*=8/25,\quad r_c=1/2,\quad K=7
\]
解释为这些准确有理数；\(w_c\) 分别为 \(1/10,3/10\)。所有长度、原半径、
cap 和伸缩均由下面的连续实公式定义，浮点积分仅是近似求值。
真正无限部分 \(n\ge160\) 仍是原来准确校准的 source，未用 finite packet
中的近似根替换其定义。两者的相接端口与谷内 \(\alpha_n\) 无关。

记
\[
 \delta_n=\delta_0 2^{-n},\quad c_n=c_0 2^{-n/2},\quad
 L_{\rm src}=6\delta_0+
       {6c_0\delta_0\over1-2^{-3/2}},\quad
 \widehat r_c=r_*e^{L_{\rm src}/\sqrt{12}},
\]
\[
 \epsilon={w_c\widehat r_c^7\over(2\delta_0)^a},\quad
 \mu_n=\epsilon\delta_n^a.
\]
原第 \(n\) 格的起点是
\[
 \log\widehat r_{n,0}=\log r_*+
 {3\delta_0 2^{-n}+
   6c_0\delta_0 2^{-3(n+1)/2}/(1-2^{-3/2})\over\sqrt{12}}.
 \tag{1}
\]
九片依次为端口、过渡、峰、过渡、谷、过渡、峰、过渡、端口；
三个平台长 \(\delta_n\)，其余六片长 \(c_n\delta_n\)。
各片局部参数 \(x\in[0,1]\)，原径向率严格为正。

原 log-level 的五个端值为
\[
 v=(\log\delta_n,\ \log64,\
       2\log\delta_n-\log\alpha_n+\beta_n,\
       0,\ \log\delta_n+a\log2).
\]
相邻端值按 \(S_5(x)=10x^3-15x^4+6x^5\) 插值；平台常值。
若当前片起始 offset 为 \(o\)、长为 \(\ell\)，则
\[
 \log\widehat r=\log\widehat r_{n,0}+(o+\ell x)/\sqrt{12},
 \qquad z_{\rm raw}=\log\mu_n+v(x)-\log\delta_n-7\log\widehat r.
 \tag{2}
\]
cap 的五个正 level 为
\[
 (.004,C_{n,1},C_{n,1}/64,C_{n,1}/64,.004).
 \tag{3}
\]
packet 实际满足
\[
 .299<C_{n,1}2^{7n/4}<.301,\quad
 \alpha_n\in[1/2,2],\quad |\beta_n|\le5.
 \tag{4}
\]

设 \(c\) 是 cap level 的 log，按同一 \(S_5\) 插值。soft log-cap
\(F(z,c)\) 在 \(z\le c-2\) 时为 \(z\)，在 \(z\ge c+2\) 时为 \(c\)。
其间设 \(t=(z-c+2)/4\)，定义
\[
 S_7(t)=35t^4-84t^5+70t^6-20t^7,\qquad
 F(z,c)=c-2+4\int_0^t[1-S_7(y)]\,dy.       \tag{5}
\]
因此 \(F_z=1-S_7(t)\in[0,1]\)、\(F_c=S_7(t)\in[0,1]\)，并且
\(F(z,c)\le\min(z,c)\)。这也证明它分别关于两个输入单调。

通常 \(z=F(z_{\rm raw},c)\)。仅第0格的末过渡 j=7 改为
\[
 z=S_5 z_{\rm raw}+(1-S_5)F(z_{\rm raw},c),  \tag{6}
\]
末端口 j=8 保持 \(z=z_{\rm raw}\)。令 \(w=e^z\)。
除第159格入口的 \(\chi=S_5\) 及第0格末端口的 \(\chi=1-S_5\) 外，
\(\chi=1\)。除末端口
\[
 j_0=1+(r_c/\widehat r_c-1)S_5
\]
外 \(j_0=1\)。准确物理径向率为
\[
 r_x=A(x)+\lambda B(x),\quad
 A=(1-\chi)\widehat r_xj_0+
   {\chi|w_x|\over7(1+w^2)^{3/2}},\quad
 B={\chi\widehat r_x\over1+w^2}.             \tag{7}
\]
这里所有自由 warp 权重为1。

## 2. 有限前24格的严格上界

fd2d_layered_positive_warp_interval.py 对 (1)–(7) 使用 mpmath 区间算术。
每片等分128个闭区间，用 integrand 的区间上界乘宽度后求和，覆盖前24格。
它不是把 Gauss 数值积分误差当作严格界。

具体地，\(S_5\) 单调；\(S'_5=30x^2(1-x)^2\) 在半区间分别单调，
全局最大值 \(15/8\)。程序据端点和 \(x=1/2\) 给它们的准确区间包络。
对于 (5)，函数值使用关于 \(z,c\) 的单调性；导数使用
\(F_z\in[0,1]\) 及 \(S_7\) 的单调性。所有 exp/log/sqrt 及积分上和都
使用向外区间计算。固定 binary64 系数先经整数分子/分母进入区间，
未把打印的小数冒充准确值。

这一段的有限区间宽度只影响所给上界的松紧，不影响其有效性。
程序把最终上端点转成准确有理数保存，upper_decimal_approx 只是展示。

## 3. 从第24格起的解析余项

本节同时覆盖尚余有限格和准确 source 起点与 cuff 的半径差。
对 \(n\ge24\)，(4) 给 \(\max e^{v(x)}\le64\)。例如谷值至多
\(2\delta_0^2e^5<64\)，其余端值更直接。原总 log 长度小于 \(.04\)，故
\[
 (\widehat r_c/r_*)^7<1.1,\qquad
 w\le w_{\rm raw}
 \le {64(.3)(1.1)\over2^{11/4}\delta_0}\,2^{-7n/4}
 <640\,2^{-7n/4}.                            \tag{8}
\]
这里 \(2^{11/4}>6\)。\(n\ge24\) 不涉及 (6) 的 cut 恢复片。

五个原 log-level 的符号和顺序已由 (4) 固定。因此其总变差，加上
\(-7\log\widehat r\) 的变差，严格小于
\[
 6|\log\delta_n|+2\log64+2\log2+11.          \tag{9}
\]
cap log-level 的总变差为
\[
 2\log(.004/C_{n,1})+2\log64
 <{7n\over2}\log2,                          \tag{10}
\]
因为 \(C_{n,1}2^{7n/4}>.299>.256=.004\cdot64\)。
利用 \(\log2<.7\)、\(\log(500/3)<6\)，(9)+(10) 小于 \(7n+64\)。
这两个基本不等式也可直接由正项指数级数得到。

由 (5) 的导数凸组合以及 (8)，得到
\[
 \int_{\text{格 }n}|w_x|\,dx
 <640\,2^{-7n/4}(7n+64).
\]
略去曲率分母中的 \(1+w^2\) 只会增加上界。设 \(q=2^{-7/4}<3/10\)
（四次方后即 \(128(3/10)^4>1\)），于是余下所有曲率项满足
\[
 \begin{split}
 \sum_{n=24}^{159}\int{\chi|w_x|\over7(1+w^2)^{3/2}}\,dx
 &< {640\over7\cdot2^{42}}
 \left({232\over1-3/10}+{7(3/10)\over(1-3/10)^2}\right)\\
 &<6.9790\cdot10^{-9}.                       \tag{11}
 \end{split}
\]

这一余段仅第159格入口有 \(1-\chi\ne0\)，且此处 \(j_0=1\)。
它的未伸缩径向项，加上深端原 source 起点到 cuff 的半径差，占据原 source
互不重叠的径向区间；总和不超过第24格及更深 source 的全部径向宽度。
其总 log 长度小于 \(.04\,2^{-24}\)，使用 \(r_*<1/2\)、
\(\sqrt{12}>1\) 及 \(e^x-1\le x/(1-x)\)，该宽度严格小于
\[
 {1\over2(25\cdot2^{24}-1)}<1.1921\cdot10^{-9}.       \tag{12}
\]
(11) 的准确有理右端与 (12) 相加，直接有理比较给
\[
 \boxed{\,A_{\ge24}+(\widehat r_{\rm deep}-r_*)<10^{-8}.\,}       \tag{13}
\]
未用任何有限深层浮点传递矩阵来控制 (13)。

## 4. 正伸缩及精确闭半径

设 \(A_{\rm all}=\sum\int A\,dx\)、\(B_{\rm all}=\sum\int B\,dx\)。
在任一主体开区间 \(\chi=1,\widehat r_x>0,w>0\)，所以
\(B_{\rm all}>0\)。若前24格区间上界加 \(10^{-8}\) 小于 \(9/50\)，则
\[
 \lambda=
 {r_c-\widehat r_{\rm deep}-A_{\rm all}\over B_{\rm all}}>0.       \tag{14}
\]
从 \(\widehat r_{\rm deep}\) 积分 (7) 因而严格单调并准确到达 \(r_c\)。
深端及 cut 的 \(\chi\) 有零两 jet，与旧端口的两 jet 相接；cut 上仍为
\(w=w_c,w_r=-7w_c/r_c\)。这仅使用准确公式，不以 float 的半径误差零代证。

wc01 的实际128等分、40位区间计算已自然 exit 0，给
\[
 A_{<24}+10^{-8}<.141748464271<.18.
\]
绑定文件为
2026-11-12-fd2d-layered64-wc01-recovery02-positive-warp-interval-n128.json。
wc03 的同一128等分、40位区间计算也已自然 exit 0，给
\[
 A_{<24}+10^{-8}<.170952310456<.18.
\]
绑定文件为
2026-11-12-fd2d-layered64-wc03-01-positive-warp-interval-n128.json。
两个 scalar packet 的 SHA256 分别为
98047e9b51a8377d5debf5ec542f429e828f6e23215ac4fe8deb403de5d31c11
和 a8e8b5091fc7497f843d32da3ca3fbeecf99458d16b531232ea5bf72678523c6。

因此上述两份输入现在均可直接调用
geometry-layered64-slope-path-budget.md 的全尾背景主曲率至多7、
严格 \(L_{\rm tail}<.188\) 以及实际尾的路径/位置/held 条件。
“已通过”仍不包括实际非圆尾的主曲率或 reach；它们取决于尚在求解的
非线性同度量场。这份证明不把背景曲率界升级为非圆曲面曲率界。
