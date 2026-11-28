# Phi：整个 D2=0 最高方向的原一元 Bézout 排除

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 完整结论

在当前一般 unit211 的 $\Phi=0,D\ne0$ 原图，整个最高共同零方向
$$
D_2=2\ell-t^2=0
$$
已经排除。此前[五个候选权对](R150-appendix-unit211-Phi-zero-highest-D2-zero-five-weight-support.md)的全部 $s$ 纤维现已一并关闭，没有剩余嵌入或重根分支。

本次从三组真实原二次式构造不除首项的纯权 cofactor，再在 $\mathbb Q[u]$ 中完成全来源 Bézout。实际首一 gcd 恰为
$$
\boxed{G(u)=(u-1)^{10}(u-2)^8.}
\tag{1}
$$
这两个因子在本整曲线上都是已付原单位，因而给出真正原单位理想。

这是当前最高方向的排除；它没有排除一般物理 $D=0$ 碰撞图，也没有排空其它最高方向或整个原仿射 Phi 图。这里不能把 $D_2$ 与原物理 $D$ 混同。

## 2. 完整原范围和整方向缩约

整 H1 已排除，第一原二次头在当前图可用。共同最高方向若有 $\lambda=0$，三个原均值可逆的 $T^2,Tz,z^2$ 头矩阵迫 $T=z=0$，故不是非零方向。因此在最高齐次式中取
$$
\lambda=1,\qquad t=T/\lambda,\qquad s=z/\lambda.
$$
这不在原仿射方程环中添加 $\lambda^{-1}$。

原矩条件的最高部分为
$$
D_2=2\ell-t^2,\qquad
K_3=4\ell^2-6\ell t+2t^3,\qquad
\overline F_6=MK_3^2-4m^2D_2^3.
$$
$M,\ell$ 已付。若 $D_2=0$，则 $K_3=0$；用 $t^2=2\ell$，
$$
K_3=2\ell(2\ell-t).
$$
所以
$$
\ell=\frac12,\qquad t=1,\qquad
Q=4(u-1)(u-2).
\tag{2}
$$
最后一式使用原 $\Phi=0$ 恒等式
$\ell=1-2(u-1)(u-2)/Q$。

在 (2) 的整曲线上，$u-1,Q$ 已付，所以 $u-2$ 也已付。保留四条原最高式
$$
h_i(u,s)=[\lambda^2]\,
F_i\bigl(u,4(u-1)(u-2),\lambda,\lambda,\lambda s\bigr),
\quad
F_i=(Rbar,W4,Obar,N1).
\tag{3}
$$
它们对 $s$ 至多二次。完整原定义、权分母及 (3) 的全部最高分解已在前稿实际返回；此次只取必要构造前缀，没有再执行旧 $\mathbb Q(u)[s]$ Euclid。

## 3. 三个包含全部首项零纤维的原 cofactor

在本节临时写
$$
A=as^2+bs+c,\qquad B=ds^2+es+f,\qquad
l_1=ae-db,\quad l_0=af-dc.
$$
这里六个字母仅为所选原二次式的系数。直接展开给出完整多项式身份
$$
\boxed{
l_0^2-l_1(bf-ce)
=(e l_1+d l_1s-d l_0)A
 -(a l_1s+b l_1-a l_0)B.
}
\tag{4}
$$
右侧的三次、二次和一次项准确消去；其常数项等于左侧。式 (4) 没有倒置 $a,d,l_1$，所以包含这些首项的全部零纤维。

对 (3) 中固定的三对
$$
(h_R,h_W),\qquad(h_R,h_O),\qquad(h_R,h_{N1})
$$
应用 (4)。本次每对完整原多项式身份都实际乘回。按原已付权分母清分母并以非零 QQ 常数归一，所得三个纯 $u$ 多项式记为 $r_{RW},r_{RO},r_{RN}$，均属于同一个原最高理想。

| 原行对 | $u$ 次数 | 项数 | 准确定义 SHA256 |
|---|---:|---:|---|
| Rbar、W4 | 24 | 25 | 6dd7d1f6b0a4fd40f432af45c56ae95c57449d08098b5e17f602164397d1c957 |
| Rbar、Obar | 26 | 27 | 2b07bdf0251acf41e5224212e9bedd365b7da1c780d041e2d898f424a88b2799 |
| Rbar、N1 | 26 | 27 | 1272b487f1d9d5212fc6f554b2ab0d1325ea7f860031455ab9ce3015ccde476a |

这些对象由 (3)–(4) 和唯一源定义，没有另存可重算系数表。

## 4. 完整 $\mathbb Q[u]$ Bézout 与原单位返回

本次在 $\mathbb Q[u]$ 中逐次作扩展 Euclid。实际 gcd 次数链为
$$
24,\ 26\longmapsto20,\qquad
20,\ 26\longmapsto18.
$$
每次除法完整乘回，始终保留三个来源，并实际给出
$$
\boxed{
G(u)=v_{RW}(u)r_{RW}(u)
    +v_{RO}(u)r_{RO}(u)
    +v_{RN}(u)r_{RN}(u),
\qquad v_i\in\mathbb Q[u].
}
\tag{5}
$$
这里的系数求逆只发生在非零有理常数上，所以 (5) 在所有例外 $u$ 值处同样成立。它不是仅在 $\mathbb Q(u)$ 泛域成立的目标。

首一 $G$ 的实际次数为 18、19 项，定义 SHA256 为
2a58c00615cd56c2aa432a3f645a9b54a3fdc9193aef48ada090a4ccdc374872。
完整精确整除只剥 $u-1$ 十次和 $u-2$ 八次，剩余非零常数，全部乘积均返回。因为 $G$ 首一，得到准确式 (1)。

将 (4) 的原来源代入 (5)，再用 (1) 的两个已付单位，可得
$$
1\in(h_R,h_W,h_O,h_{N1})
$$
于当前整曲线的原已付权环中。因此不存在任何复 $u,s$ 的共同零点。这一结论包含前稿四次因子的所有复嵌入、一次因子的完整平方零支及每个 $s$ 纤维。

源码还构造了原三均值头及已付的 $m,u+Q-1$，但最后的 (1) 只用了 $u-1,u-2$，其余因素没有参与单位剥除。上述单位理想证明因此没有依赖一个新的头特化判空门。

结合 (2)，当前整个 $D_2=0$ 最高方向已排除。剩余最高共同方向必须满足 $D_2\ne0$；不能把这一最高环结论改写为其它原仿射分支已空。

## 5. 唯一实际执行

[唯一新源](../notes/2026-11-28-unit211-Phi-zero-whole-D2-infinity-original-weight-cofactor-unit-8542.py)和[执行前完整输入](../notes/2026-11-28-unit211-Phi-zero-whole-D2-infinity-original-weight-cofactor-unit-8542-input.md)：

- 源 blob：297a59c19e56196101af746bd881e444f3b809b8。
- 6821 字节，SHA256 be4e95231be36d1de37a33a76abf87dda587a982cb7b77df0a8318c346eb4b90。
- [run 46089340267](https://github.com/Rogerhu12/math-research-public/actions/runs/46089340267)，job 140806323973，attempt 1。
- 真正 driver 0.115540560 秒，最大子进程 RSS 40008 KiB，内层 exit 0。
- 源最终阶段 0.057568870 秒，源报告峰值 39448 KiB。
- stdout 3633 字节，SHA256 f5650a6da1822239dcd109061b16f4e159f716abef3d34e759dafb4d5749437a。
- 冻结源提交及实际 pull 后提交均为 86cf860e85d7aa440e67ec1c616ae856c947a99c。
- 2026-11-28 00:42:51.664837 UTC 真实 pull，两份 README 无变化。

必要原定义前缀 5615 字节，SHA256
6565773e131c79cb1f2c1a1155f4059ae0e33d724e11db284ab345c06c2b8326。
本次未执行旧泛域 Euclid、旧 Gaussian、P6/P9、范数或大模块，保存范围限于源、定义、SHA 与[实际小回执](../notes/2026-11-28-unit211-Phi-zero-whole-D2-infinity-original-weight-cofactor-unit-execution-8542.json)。

整 Phi 原值图、余最高方向和 ordinary ISP 继续处理。
