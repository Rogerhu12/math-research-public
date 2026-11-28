# 新输入：正确 Phi 的整 B=0 有理曲线与原线性余式

日期：2026-11-28（Asia/Taipei）。尚未执行；120 秒 / 1 GiB。

源码：[2026-11-28-unit211-Phi-zero-true-Bzero-rational-original-six-by-two-8542.py](2026-11-28-unit211-Phi-zero-true-Bzero-rational-original-six-by-two-8542.py)。
源码 SHA256：f027f52d63a345ce89b05ecbce7276093256eaf5a4b0ff9bf59da0e123a5f835。
唯一依赖：2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py，SHA256 5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7，放在同目录或 ISP_INPUT_DIR。只读取构造 quads 之前的必要原定义，不运行四头测试。

令 $s=u-1$，原曲线
$$
B=-Q^2+(12u^2-20u+8)Q-16s^2=0.
$$
在当前 $Q P_fP_{02}bc(1-Q)\ne0$ 原图，$s,Q$ 非零。取
$$
x=\frac{Q}{4s},\quad u=\frac{(x+1)^2}{3x},\quad
Q=\frac{4(x^2-x+1)}3.
$$
两向身份都在源中完整返回；不漏参数无穷点，因为每个有限原 $u,Q$ 都给有限非零 $x$。同点
$$
1-Q=-\frac{(2x-1)^2}{3},\quad
\ell=\frac{(x+1)(5x-1)}{6x^2},\quad
bc=\frac{(x+1)^2(7x^2-4x+1)}{36x^4}.
$$
因此本输入仅把
$$
x(x^2-x+1)(x+1)(2x-1)(5x-1)(7x^2-4x+1)
$$
的因子当作已付权单位。原 $A=4s^2-Q=-4s(2x-1)(x+1)/(3x)$ 在本曲线上也由这些原单位非零，不依赖别处的旧头结论。

新的四二次仍为真正 $\overline R,W_4,\overline O,N_1$。前三均值头在此精确秩至多二；源不重复上一整 A 门，而选择第一个符号非零的三行头（优先 $\overline R,W_4,N_1$），完整 adjugate 只在其非零图生成三规则。其剩余一原式成为 $\lambda$ 次数 $(2,1,1)$ 的三列线性余式。所有新纯 $x$ 头零纤维保留并因式记录。

若新的 $2\times2$ 斜率不恒零，使用同一点的中心坐标解掉该线性式；三原二次真实组合给首一 $\omega^2+\beta_1\omega+\beta_0$。三一次余式及其真实 $\omega$ 倍构成完整六乘二呈示。每项分母只允许来自原 paid 乘积和本次明确保留的头、斜率。若斜率恒零，则准确停在该结构，不宣称两生成元。

本次目标是整未付 B 曲线上的新原呈示及有限参数例外支持；不是排空声明。没有倒物理 D、没有模空性提升、没有重放旧错误均值、已冻 GB 或 A 的固定 QQ 结式。
