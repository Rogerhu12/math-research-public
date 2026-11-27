# 原 full47 已完成 q² CM 对数与 Gaussian/Jacobi 来源的独立交叉核

日期：2026-11-27（Asia/Taipei）。

**状态：算法与归一化已明确；本文件不预报数值比较结果。**
新的消费者只读取已经完成的四条 q² 对数，复建固定原 Hodge 基底和 $T_2,T_3,T_5$ 的有限矩阵，然后逐项比较。它不重做 CM 链、47挠点 grid、高 Gaussian 矩、Jacobi 路径、全局高度或 QC。

## 1. 两个已经完成的输入及应比较的量

固定 $X=X_{\rm ns}^+(47)$、$q=4513$。令
$$
u_D=23[y_D]-C_\infty,\qquad
B_q=q+1-T_q,\qquad
\lambda(D)=q^{-1}\log(D)\pmod q.
$$
四个基本 CM 标签为 $141,0,76,108$，对应判别式 $-4,-3,-7,-8$。

原 Gaussian 高矩的公开来源是 source
282be088b6286c21e4ccedf79127c8a1f93e77df、
run45947023569/job140333947037。其完整73维向量是
$$
\lambda_4=\lambda(B_qu_{-4}),
$$
SHA-256 为
489ab09b0e7bedae211e478938e687b51cd3d477438d9d47605d2cac0a4929dd。
旧 height 请求还保存同一向量在16个原归一一次本征形式上的读数。

新 q² 来源是：

| 项目 | 固定值 |
|---|---|
| source | ccad9f4ad40466d9a3387e70b42a77c75a2d75b9 |
| run / job | 45977769585 / 140433713916 |
| request SHA | 5bf66b6ddb303f71e2c255badc61942d0faf6694612a9ebdf74adde9b5dc49dc |
| 完整 receipt.completed SHA | 5a084d55b4df85ab0a4eb38e8e5032292960ff83a81b6babfd3c54235d5ea734 |

四条 `actual_CM_first_log` 的准确除子均为 `23*y-C_infty`，读数已经除以 $q$。完整向量 SHA 为：

| 标签 | $\lambda(u_D)$ 的 SHA-256 |
|---:|---|
| 141 | 5e33d5638db673d62465a2c48415558e239adb07e50a411582c833be4bd2ccb3 |
| 0 | c5292bd60325292f2b006fc7e1330508f0d6e9e1d812aedcc629d28064bba44b |
| 76 | ea56dbbe7450aa404c5301e6fb23115a2c0afa1f79dba1b5cda08f395bb63807 |
| 108 | dadb68c6004ffaafcf0f15ba67a7957cc291258c6c49654ddca07e02c6e2e1e7 |

这四个 hash 本身没有理由与 $\lambda_4$ 的 hash 相同。首先必须比较
$$
B_q\lambda(u_{-4})\stackrel{?}{=}\lambda_4.
\tag{C1}
$$

## 2. 原 q² 终点的符号和 Hodge 归一

q² 来源使用的73维 Hodge kernel SHA 为
a1631dfbb9f6db6f796fe17e634869d57fe9486f276bcedc200a10c4ebfac86d，
与旧 Reynolds source 的原 kernel 完全相同。

在原 Tate 参数 $t$ 中，实际微分为
$$
\omega_i=47G_i\,dt/t.
$$
取原 pencil $z=F_0/F_1$，则源码中的
$$
W=\frac{t(F_0'F_1-F_0F_1')}{47}
$$
满足
$$
\frac{\omega_i}{dz}=\frac{G_iF_1^2}{W}.
\tag{C2}
$$
有限留数代数将 $G_i/F_1$ 除以 $W/F_1^3$，故得到的正是 (C2)，没有遗失宽度47或重新选择微分标架。

设有符号链给原类 $\epsilon ND$，强制终点 add-flip 后得到其负类 $-\epsilon ND$。终点截面写成
$$
h_{\rm new}=F_0F_1+q\,\Delta.
$$
其局部点位移为 $z=-q\Delta/F_1^2$。因此
$$
\lambda(D)_i
=\frac{\operatorname{Tr}_{A/\mathbf F_q}
       ((\Delta/F_1^2)(\omega_i/dz))}
       {\epsilon N}.
\tag{C3}
$$
本次四条记录均有 $\epsilon=-1$、$N\bmod q=551$，且源码已经在 (C3) 中使用这个符号。消费者不能在输出上再乘一次 $-1$。它逐条验证原终点公式、实际 $D_0$ 归约、完整有限 étale 留数代数和全部共轭均已保留。

## 3. 原 Hecke 行作用与 Jacobi 比例

原 Hodge 矩阵的约定是
$$
T_n\omega_i=\sum_j(M_n)_{ij}\omega_j.
$$
利用实际自伴 Hecke 对应，
$$
\lambda(T_nD)_i=\sum_j(M_n)_{ij}\lambda(D)_j.
\tag{C4}
$$
所以列向量由 $M_n$ 左乘；这里不转置。

消费者只调用原 Hodge source 的固定95描述子复建和已付有限 `hecke_bridge`，逐个核 $M_2,M_3,M_5$ 及 $H_2=M_2+2M_3+4M_5$ 的旧 hash。然后取
$$
H=M_3+M_5.
$$
它核原 $H$ 全矩阵及73次特征多项式 hash，直接消费 R1120 已认证的 $B_q(H),\rho_D(H),c_D(H)$。不再计算模符号或 $T_q$。

R1119/R1120 的比例为
$$
u_D=\rho_Du_{-4},\qquad
c_D=\rho_DB_q^{-1}.
\tag{C5}
$$
原标签、判别式、$r=0/2209$、粗权1及反向 incidence 权 $2,3,1,1$ 均逐条核对。四条 $\rho,c$ 的完整记录 SHA 为
b9f610583ea037e18d5e948341af5b09b78c8426a16f7643a6f44bd2949b882e，
证书 SHA 为
4a4895f692c0eaeab0fa76eed9987af0ebaefa524d03d23fcb00425c2df45ed8。

此外保留独立的完整矩阵桥
$$
I-B_q(H)=\overline T_q=C_{\rm row},
\tag{C6}
$$
核 Cartier row 与其 transpose 的两个旧 hash，以及 $\det B_q=551$。不以 determinant 相同代替 (C6)。

## 4. 有限交叉核及失败语义

先形成 $\lambda_4^{\rm new}=B_q(H)\lambda(u_{-4})$，比较其完整 SHA 与旧 $\lambda_4$ 的 SHA。这不用再生旧 Gaussian 高矩。

随后对全部四条73维列同时比较
$$
\begin{aligned}
\lambda(u_D)&\stackrel{?}{=}\rho_D(H)\lambda(u_{-4}),\\
\lambda(u_D)&\stackrel{?}{=}c_D(H)\lambda_4^{\rm new},\\
B_q(H)\lambda(u_D)&\stackrel{?}{=}\rho_D(H)\lambda_4^{\rm new}.
\end{aligned}
\tag{C7}
$$
后两式保留 QC 生成元归一，也交叉核程序的多项式作用；它们不替代第一条独立 Gaussian anchor 比较。

最后读取旧16个 $H_2$ 一次本征形式。对每个固定本征值重建其一维左本征空间，依旧规则将首个非零原 Hodge 坐标归一为1，核旧本征向量 hash，再比较其在 $\lambda_4^{\rm new}$ 上的值与旧 height 请求中的真实读数。

每项输出实际/预期 hash、相等布尔值和有限首批差坐标。即使 anchor 不相等，也继续打印其余比例与16次读数，从而区分整体归一问题和个别比例问题。程序不猜测新符号、比例或基底变换，不自动修正任何输入。

全部比较完成后：

- 全相等：`status="complete", comparison_status="match"`，退出码0。
- 某个比较不等：`status="complete", comparison_status="mismatch"`，退出码2；这是已完成的数学不相容报告。
- 输入来源、旧 hash、下载或实际计算未完成：`status="incomplete"`，退出码1；只保留明确已完成的项目。

因此本方法正文不预先宣称新旧来源相容，也不据一次未完成下载推翻任何旧结论。

## 5. 日志读取、请求和预算

新文件：

- `scripts/full_p47_CM_log_crosscheck.py`；
- 本方法文件。

新请求固定 `execution_id="full-p47-CM-log-crosscheck-v1"`，
`prime=47, coefficient_prime=4513, sage_version="10.6"`，
总预算600秒、reserve30秒，并保存第1节的来源标识与 hash。
`source_sha256` 至少覆盖新脚本、本方法、原 Hodge 脚本、
旧 height 请求和旧 QC-v2 请求。
请求和脚本均不保存四条73向量或完整 clean records。

runner 仅从固定 job140433713916 的日志取输入。首个请求发至固定 GitHub Actions API，使用该 workflow 的只读自动 token，并禁止自动重定向。取得302的 HTTPS Location 后，使用全新、无 Authorization 的请求下载日志；任何后续跳转也不得携带 Authorization。不输出 token 或临时签名 URL。

日志只驻留 runner 内存。消费者要求唯一、完整、来源相符的 receipt，重算其 `completed` 的 canonical SHA，再读取四条 CM 记录并核各自73向量 SHA。workflow 只需 `contents: read` 与 `actions: read`，通过 `GH_TOKEN` 传入自动 token。没有 artifact、Release、raw 数组提交或新缓存。

整个算术入口仅限指定公开仓库的 Actions；Sage10.6，单进程，无 python-flint wheel、无扩域 worker。这里只有固定有限矩阵的输入复建和新的交叉比较。
