# Phi=0 的主二次头零支：原均值 T 闭包与单位六次目标的 C71,29

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 原范围与新结论

本稿接
[R150-appendix-unit211-Phi-zero-rho-head-zero-main-original-unit-necessary-curve.md](R150-appendix-unit211-Phi-zero-rho-head-zero-main-original-unit-necessary-curve.md)
的主分支
$$
d=b-c,\quad \rho=-d,\quad v=d^2,\qquad
\ell=1+2v,\quad u=1+v,\quad Q=1-v.
$$
全部原 unit211、LS、物理 $D\ne0$ 的已付单位继续保留。$\Phi$ 的 $\rho$ 二次头为零时另有 $d=\pm\frac12,\ell=\frac32$、自由 $\rho$ 的特殊权支；它们由其他原输入处理，不能用本稿覆盖。

本次原均值/N1 的真实 $T$ 闭包与同一点单位六次目标，给出新的必要式
$$
C_{71,29}(v,\lambda)=0.
$$
它的双次数为 $(71,29)$，共 2111 项，完整精确系数已保存。没有宣称它是旧必要式的因子、没有宣称新旧两式互素，也没有排空该主支。旧 $C_{87,55}$ 仍是已登记的必要式；本次不为恢复它的系数重做旧六行行列式。

## 2. 原首一六维矩关系

沿用
$$
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_2-T^2,\quad
s_n=\ell B_3-A_2T,\quad
K=\ell^2B_3-3\ell TA_2+2T^3,
$$
$$
S_n=s_n+(3-2\lambda)D,\qquad Z=u s_n-2TD.
$$
令 $m=u-\ell$、$M=\ell(2u-\ell Q)-u^2$。原矩关系为
$$
F_6=M K^2-4m^2D^3=0.
$$
其 $T^6$ 首项为已付权单位 $4\ell^2(1-Q)$。所有乘法按该真正首一关系约化，保留同一个原 $T$。

主支具有
$$
T_0=-1-3v,\qquad J-Q=-4v^2,\qquad u+Q-1=1.
$$
系数只需要 $v,\lambda$。形式值对偶仍按 $r^2=v$ 表示原 B/C 两值，实际 $\rho=-d$ 的两个符号对应原 B/C 交换；没有把一个形式值为零拆成两个系数为零。这里原 B/C 两个方程都存在，且 $r\ne0$，所以其 even/odd 分解有完整原来源。

显名几何分母仍只有 $D$ 与 $P=S_nZ$。原
$$
S_n=DS,\qquad Z=2mD\zeta
$$
保证
$$
U=D S_n Z
$$
在实际原点非零。没有倒置商代数范数或临时消元主元。

## 3. 新行输入与完整同点身份

本次只用四个原多项式
$$
E_1,\quad E_{B,\mathrm{even}},\quad E_{B,\mathrm{odd}},\quad N_1
$$
及它们乘 $1,T,\ldots,T^5$ 后的实际六列向量。全部 24 个候选行都由原矩关系逐次约化，清去的权参数分母都已核为原单位。

实际选定六行是
$$
E_1,\quad E_{B,\mathrm{even}},\quad E_{B,\mathrm{odd}},\quad N_1,\quad
T E_1,\quad T E_{B,\mathrm{even}}.
$$
数值模点只用于选出行号；结论依靠随后完整 QQ 行列式恒等式。本次目标为原 $U^6$，不是旧主稿使用的 $U$。旧主稿的 NB 六行矩阵没有被重复计算。

记所选矩阵为 $A$，目标的六列为 $w$，$\Delta=\det A$，$\Delta_i$ 为用 $w$ 替换第 $i$ 行的原行列式。程序实际逐项乘回 385 次 Bareiss 除法，并对全部六个坐标核验
$$
\Delta w=\sum_{i=1}^6\Delta_i A_i.
$$
$\Delta$ 的双次数为 $(90,71)$，6275 项。七个多项式的完整共同因子 $g$ 双次数为 $(17,42)$，632 项。除去同一 $g$ 后再次核验六个完整坐标：
$$
\frac{\Delta}{g}w=\sum_{i=1}^6\frac{\Delta_i}{g}A_i.
$$
因此该身份在 $g$、临时主元或原行列式为零处仍成立；它没有除去这些零纤维。

最后只剥除与原已付 $Q,T_0$ 各自相交的 gcd 因子，并逐次完整乘回。日志中的各一次是实际 gcd 来源标签，不是整条同名多项式的幂声明。由原六行均为零且 $U^6\ne0$，得到所述
$$
C_{71,29}(v,\lambda)=0.
$$

## 4. 精确新输入与执行

三变量规范表示（$T$ 指数恒为零）的多项式摘要为
`6888e4c17a3c4b3f0791a5e9101440dabc201ebfd004a175a4f564808741c081`。
完整二变量 $(v,\lambda)$ 系数以压缩 JSON 保存，且源内实际解压、重建并检查相等。因此后续真正的新因式、纤维或补输入可以直接取该载荷，无需再次计算本六行 Cramer 返回。

原源：
[2026-11-27-unit211-Phi-zero-main-head-zero-mean-T-unit-six-v-input-8542.py](../notes/2026-11-27-unit211-Phi-zero-main-head-zero-mean-T-unit-six-v-input-8542.py)

- Git blob：`e444311f414206047ce76c59c4509db2bef6674b`。
- SHA256：`b4413d1e37bdce9aaba5a18bb2eee487c6103cad686a6e243e8d2a5c20e80d07`。
- 实际 run/job：46023122692 / 140587572877。
- source commit：`1d7725748854975d5f60c39cdbf9e65c6b17e2d9`。
- 内层退出码 0；43.208444069 秒；89032 KiB。
- stdout：66869 字节；SHA256 `d47bdbb36fe33b5b1e9d8689feb337e4e74d8bd67e3203d14c76f71ed77c1809`。
- 执行前真实 pull 的两份 README blob 均无变化。

本次完整四个原均值/N1 行在 0.891 秒返回，24 个真实 T 闭包候选在 1.045 秒返回，完整单位目标共同消去在 43.107 秒返回。最终源正常结束，没有把后续因式分解或整套旧输入重放设为本结论的成立条件。
