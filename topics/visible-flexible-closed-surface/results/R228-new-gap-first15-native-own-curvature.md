# R228：新 gap 原生 ramp 前 15 单元的完整连续自身曲率

会话：Astra-visible-flex-6a65；日期：2026-11-26。依赖 R227 的同一实际有限位置场。

## 已完成的结论

对 R227 定义的整个前 15 个原生 Fourier–Hermite 单元，所有连续径向位置和全部角圆周上的两个主曲率满足

$$
\max(|\kappa_1|,|\kappa_2|)
\le\frac{390868699751529326143218701575}{39614081257132168796771975168}
<9.866914<10<\frac1{.097}.
$$

这里算的是完整 Cartesian 位置场**自身**的第二基本形式与主曲率；没有代入 Cauchy 流的辅助 $n,m$ 或借用准确 coast 的曲率。所有 768 个保存位置 Fourier 系数都被保留，前 15 单元以 $15\times64=960$ 个闭参数盒覆盖，实际不需分裂。

这仍是原生 raw 位置场的证明。第 16 个准确 coast 端口修复单元、`WarmMaster.normalized` 的径向缩放与依赖 $s$ 的角逆、全局嵌入与 reach 均不在本结论内。

## 1. 同一输入与完整角尾

输入 master、R227 的全域 Gram 报告及本次源码 SHA256 为：

```
master: 0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7
R227 report: be77c270f9dcd4c2d146ba11e961c1535ea7c810f7d916d8554942e9d97c3642
source: 2bd80a8b87d432ee23a0f43e9e629cd9b0dc274a65e073fb83a15626644f70fc
```

源码 `6a65-geometry-ramp-native-curvature-certificate.py` 直接复用 R227 的 `ActualRamp.cell`。这保证节点、物理单元长度、准确 dyadic 位置系数、首端准确中央柱覆盖及所有保存频率的含义不变。

低频部分仍选 $|k|\le95$。对于五个曲率所需导数

$$
Y_s,\quad Y_\theta,\quad Y_{ss},\quad Y_{s\theta},\quad Y_{\theta\theta},
$$

余下 $95<|k|\le384$ 的每一个保存系数按真实物理 $L^{-r}$ 与角 $k^q$ 权重进入准确 Bernstein $\ell^1$ 上界。该上界作为 Cartesian 向量误差加入低频盒，因而最后的盒包住完整场而不是截断场。

## 2. 每个闭参数盒上的完整两 jet

每个物理单元有准确多项式

$$
Y(t,\theta)=\sum_{j=0}^5 C_j(\theta)t^j,\qquad 0\le t\le1.
$$

对任一角胞中心 $\theta_0$、半宽 $\delta$，每个低频系数函数的第 $q$ 阶角导数使用

$$
C_j^{(q)}(\theta)\in C_j^{(q)}(\theta_0)
 +[-\delta,\delta]C_j^{(q+1)}(\theta_0)
 +\left[-\frac{\delta^2M_{j,q+2}}2,
         \frac{\delta^2M_{j,q+2}}2\right].
$$

其中 $M_{j,q+2}$ 是该准确有限 Fourier 系数的全局加权绝对和。中心三角函数值由已经发表的 96-bit 整数定向区间算术、Machin 型 $\pi$ 区间及带余项的三角 Taylor 公式计算，没有库三角浮点值参与真假判断。

对于径向子区间 $t=t_0+\ell v$，把相应物理导数的次数 $5-r$ 多项式准确转为 $v\in[0,1]$ 上的 Bernstein 形式，再取控制区间的凸包。最后加入上述完整高频尾，便得到五个真实 Cartesian 导数的连续包含盒。实际 960 个盒都直接使用整个物理单元，无径向子分裂。

这一步的 Taylor 中心用于构造覆盖区间，不是用中心点曲率替代盒内曲率。

## 3. 真实 Gram、单位法向与正交 shape 矩阵

R227 已独立证明准确场的 $E,F,G$ 误差。此处在同一盒中利用这些紧界：

$$
E\in[1-\varepsilon_E,1+\varepsilon_E],\qquad
F\in[-\varepsilon_F,\varepsilon_F],
$$

$$
G\in b(s,\theta)^2+[-\varepsilon_G,\varepsilon_G].
$$

这里 $b=(f/a_\ell)\sqrt{A^2\sin^2\theta+B^2\cos^2\theta}$，仍是 R227 的原生角目标；不是将 $G$ 误写成 $f^2$。$f/a_\ell$ 由单调 $J$ 的准确径向端值包含，角向椭圆速度平方由 $\cos2\theta$ 的局部 Taylor 盒和全局 $[B^2,A^2]$ 相交得到。

令

$$
D=EG-F^2,\qquad
\nu=\frac{Y_s\times Y_\theta}{\sqrt D}.
$$

R227 的浸入结论以及本次各盒的 $D>0$ 检查保证此式有效。分母是同一位置场真实 Gram 行列式；因此 $\nu$ 是它的单位法向。

写真实第二基本形式

$$
L=\nu\cdot Y_{ss},\qquad
M=\nu\cdot Y_{s\theta},\qquad
N=\nu\cdot Y_{\theta\theta}.
$$

在由 $(Y_s,Y_\theta)$ 做 Gram–Schmidt 得到的正交切向标架中，shape 矩阵准确为

$$
S=\begin{pmatrix}a&b_1\\ b_1&d\end{pmatrix},
\qquad a=\frac LE,
$$

$$
b_1=\frac{M-FL/E}{\sqrt D},\qquad
d=\frac{EN-2FM+F^2L/E}{D}.
$$

故两个真实主曲率的最大绝对值是

$$
\frac{|a+d|+\sqrt{(a-d)^2+4b_1^2}}2.
$$

源码对该准确表达式实施整数定向区间运算。每个闭盒的上端严格小于 $10$ 才被接收；所有盒覆盖整个 $t\in[0,1]$ 与角圆周，故得到开头的全域结论。

## 4. 已返回的实际进程回执

完整执行已在执行环境失联前返回自然 `exit 0`。外部耗时 $32.228484125$ 秒，峰值 RSS $40444$ KiB；960 个叶、0 次分裂，最坏证书单元为编号 $8$。全报告与日志 SHA256 为

```
report: be5312aec4917138d72ee4285efd48c49612bb431bbef3323bd72ebe9b5acfc5
log: ea84776445fe6db3e9652f048bba01d944f0dfa7b2f62804966da4db0d90a892
```

这两个摘要来自已实际返回的计算。随后环境重置使本地原始临时文件丢失；本文没有伪造同 SHA 报告或宣称它目前仍在磁盘。源码已从完整工具写入正文恢复，并经本地 `sha256sum` 核验逐字等于上述原源码 SHA。

各单元已返回的上界数值（准确有理上端保存在原报告中）如下：

| 单元 | 曲率上界约值 |
|---:|---:|
| 0 | 9.06977685325 |
| 1 | 9.07398668351 |
| 2 | 9.08526701737 |
| 3 | 9.10166876056 |
| 4 | 9.11811911926 |
| 5 | 9.12933680374 |
| 6 | 9.20400045422 |
| 7 | 9.83397170237 |
| 8 | 9.86691316188 |
| 9 | 9.25640088366 |
| 10 | 9.12815804411 |
| 11 | 9.11190090678 |
| 12 | 9.08941409213 |
| 13 | 9.06440343653 |
| 14 | 9.04331245940 |

每一行均由 64 个整角胞乘整个物理单元证明，并非 64 个点的采样最大值。

## 5. 复生与接续范围

先按已经发表的新 prefix 源码重新生成临时 master，并自报这次实际文件身份；再运行已发表的 R227 checker，得到绑定该 master 的真实 Gram 报告。随后执行

```sh
python scripts/6a65-geometry-ramp-native-curvature-certificate.py \
  --master "$actual_master" --gram-report "$actual_gram_report" \
  --scripts-dir scripts --angular-cells 64 --curvature-cap 10 \
  --output "$fresh_outside_git_curvature_report"
```

重生是为继续消费丢失的工作输入，不是另一个新的数学发现。新回执及 SHA 必须如实记录；只有真实内容一致才可说复现同一有限场。

当前代码同时输出全单元的 $|Y|,|Y_s|,|Y_{ss}|,|Y_\theta|,|Y_{s\theta}|,|Y_{\theta\theta}|$ 准确连续上界，供随后径向缩放的 $C^2$ 扰动预算使用。准确角重参数保留几何曲率，但依赖 $s$ 的角逆会改变 $E,F$；这条链仍须显式支付，不能用 Hausdorff 距离或已得 raw 曲率代替。末格真实 coast 端迹的完整差同样仍待支付。
