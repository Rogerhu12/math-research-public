# 2026-11-15 原 p41 高度输入接续：R781 准确 Laurent 工程

会话：serre-public-astra-20261115。状态：**运行前工程与算法证明；尚无本次实际系数结果。**

## 读取检查点与不重复范围

已读根 README、课题 README、HANDOFF、open，以及 R774、R778、R781、R777 方法和对应核心/包装源码。旧 R781 Laurent 草稿没有进入远端 main，本次从已推的 R781 证明重建核心。R774 已完成的原 H³ 不再重算；R775/R777 选基工作不由本阶段执行。

根 README 第 15 条于提交 137c5a877fb387a82cbde01f084d1fa67ee717aa 再次修改，已读取新条文：可重算数据不入 Git 或 Release。只登记脚本、参数、run、输出 SHA 和小结果摘要。跨当前计算的续接文件只作为一日的临时 active checkpoint 传输，用后删除；不把它们作为持久交付。前一版“上传 Release”的工程未发布，本方案不调用 Release。

本次执行环境在核心写出并完成 Python AST 语法解析后 unavailable。包装和 workflow 的后续文本由 GitHub 小文本 blob 保全，root 统一组装提交。没有运行本地数学，亦不预称 Actions 成功。

## 只消费真实 R774 的输入

原 producer 为公开 run 43631427773，源提交
93056f04536e61ccdd486674003b4d1380a27475，artifact 14128247134。

- artifact 名：serre-global-R774-original-p41-Hodge-cube-43631427773-1；
- ZIP SHA-256：91d9f6d926dc2a649d5fd401b9881cc6f88f8e233724408fbce8dcba109d1f0b；
- manifest SHA-256：4d97bb53b106fa53958a943f9ae9e5d00870f7cf774d4617a727b3fa857ac222；
- 小证书 SHA-256：aea27ac34e9a82203f723af27265db3cbd8d75e615247e11e0591fb2ed249b59；
- producer core SHA-256：b7e8bf0f7b629881d973afaec01a2b905c4100573d46920841a9d48489e597fa。

本阶段只读取原尺度文件及首五个 qY 块，使用至 143 阶。真实 e=1、原映射 index4、degree1206 都从该 producer 证书核实，未另选短向量或映射。包装按 run/source、artifact digest、原 manifest 和逐文件 SHA 验证来源。

## 整数域运算和真实切向相位

沿用 [R781](../results/R781-original-tangent-descent-and-inverse-free-Laurent-relations.md) 的
$v=\xi^{-10}u$。对每个 $1\le n\le143$、每个原 $b^i,sb^i$ 坐标，先乘 $\xi^{10n}$，在 $\Phi_{41}$ 下约化，再逐项验证

$$
c_r=c_{41-r}\qquad(1\le r\le20),\quad c_{40}=0.
$$

任一原行不满足便失败，不能以平均或投影强行制造实系数。通过之后用整数 Chebyshev 多项式转成 $t=\xi+\xi^{-1}$ 二十坐标。

$\lambda$ 从实际 $b$ 最小多项式的每个既约分母提取，$B=\lambda b$ 的 monic 多项式必须整系数。字段仍是原 $M^+=L(t)$，目标 $b=B/\lambda$ 未变。域元素存为 primitive 280 整数向量乘一个有理尺度；零和符号采用唯一表示。

乘法用 R781 的 $r+39i+507j$ 打包。先以 $s^2=-3$ 折叠，再用两个准确整数矩阵分别按 $f_B(B)$、$g_{41}(t)$ 约化。所有生成输入都绑定原字段多项式及尺度。无 $\kappa^{-1}$ 或从模素数近似抬升的步骤。

## 每阶只增加一个卷积系数

令

$$
W=R-wR',\quad P=R^2,\quad Q=W^2,\quad
U=P-c_*w^2,\quad V=U^2.
$$

此前已完成到 $n-1$。临时置 $R_n=W_n=0$，计算

$$
P_n^0=\sum_{i=1}^{n-1}R_iR_{n-i},\qquad
Q_n^0=\sum_{i=1}^{n-1}W_iW_{n-i},
$$

$$
U_n^0=P_n^0-c_*\mathbf1_{n=2},\qquad
V_n^0=2U_n^0+\sum_{i=1}^{n-1}U_iU_{n-i},
$$

$$
E_n=Q_n^0+\sum_{i=1}^{n-1}Q_iW_{n-i}
 -V_n^0-\sum_{i=1}^{n}\widetilde A_iV_{n-i}.
$$

于是严格取

$$
R_n=\frac{E_n}{3n+1},\qquad W_n=(1-n)R_n.
$$

真实新系数为
$P_n=P_n^0+2R_n$、$Q_n=Q_n^0+2W_n$、
$U_n=U_n^0+2R_n$、$V_n=V_n^0+4R_n$。
因此原微分恒等式第 $n$ 阶的差等于

$$
E_n+3W_n-4R_n=E_n-(3n+1)R_n=0.
$$

各内和只使用已完成系数，每阶 $O(n)$ 域乘法。$\widetilde A_n=\kappa_{n+1}\kappa^{n-1}$ 和 $\kappa^n$ 同阶保存。每个阶段只保存这八个新系数，不重复保存整个历史；阶段链绑定前一文件 SHA，恢复时直接读取旧系数，不再次进行已成卷积。

预算或异常只停止当前 run；全部已完成阶作为当前活动检查点保留，下一 run 用相同 core、原 producer 和配置续接。脚本将运行前成功、部分阶段和最终成功明确区分。

## 后续原关系矩阵

本次成功也只意味着 R781 的 $R_0,\ldots,R_{142}$ 和精确字段输入已得。它尚未构造

$$
246^3\kappa^{n+2}A_n+
\sum_{j=0}^{n+1}\kappa^jR_{n-j+1}B_j=0,
\qquad -1\le n\le141,
$$

对应的 $2860\times3028$ 原 $L$ 矩阵。最终一阶所需 $\kappa^{143}$ 可由已存 $\kappa^{142}$ 与 $\kappa$ 再乘一次。该矩阵必须再接 R777 的真实准确基；一个非零 $(A,B)$ 只有全部准确代回通过才由 R778 认证为原函数。

实际 $\beta$、第二类周期、Poincaré 纤维、真实高度 jet 和 R724 Bézout 证书都未由本阶段输出。固定 $p=41$ 输入工程不等于全 $p$ Serre 一致性；完成标准保持不变。

## API 依据

实现只使用已核对的 python-flint 0.9.0 官方接口：
[fmpz_poly](https://python-flint.readthedocs.io/en/latest/fmpz_poly.html) 的整数多项式、content、coeffs 和 monic 余式；
[fmpz_mat](https://python-flint.readthedocs.io/en/latest/fmpz_mat.html) 的矩阵构造、索引与乘法；
[fmpq](https://python-flint.readthedocs.io/en/latest/fmpq.html) 的准确有理数、gcd、numer 和 denom。正式算术仅公开仓库 Actions。
