# 两条完整权零自然通量：首次公开实际结果

日期：2026-11-15；会话 Astra-new-mechanism-9974ea84。完成的是两个新的完整函数观察，主课题尚未完成。

## 1. 实际入口与来源

公开 run [43775998866](https://github.com/Rogerhu12/math-research-public/actions/runs/43775998866)，job 133002325378，source d47749f7289ba0965e912a0e0e026bc619ebd4cb，2026-11-15 23:39:37—23:40:06 UTC，结论 success。

脚本为 [literature_weight_zero_natural_flux.py](../scripts/literature_weight_zero_natural_flux.py)，42478B / SHA256 be12b9338cf5558eacb4d05b43f201871fae5d4262dd330304eaa56df3c2e12f；参数为 [request-weight-zero-natural-flux.json](../computations/request-weight-zero-natural-flux.json)，8446B / SHA256 ad26ae977549b084dce83a7c96c5c43fe3955af7d8399907c696b7468e9c1c1d。运行沿 [完整新观察设计](weight-zero-natural-flux-two-target-design-20261115.md)，34份绑定含31旧科学源码、新入口、规则reader和workflow。Python3.12.14，纯标准库。

执行命令由workflow按顺序给出同一request：先新增八项人工的 --development，再执行不带 --development 的唯一科学入口，各 --out 仅指 runner 临时路径。原两份完整日志、原成员证明、原根/diagonal SHA 均精确核合；不重新算原 pure/self/秩。

## 2. 完整函数结论

设 $p=u'$、$r=u''$。两个原完整 pure/self 零代表均保原 $N_0$、$\Gamma$、二阶及三阶 history、同一右锚和所有真实左常数。新观察严格是
$$
n_2(u)=\Lambda_u(H_*),\qquad n_6(u)=\Lambda_u(J_6),
\qquad \Lambda_u(V)=-4\int u'''M_{-2}(u,u).
$$

结果是
$$
\boxed{n_6\equiv0,\qquad n_2\not\equiv0.}
$$

$H_*$ 的整个新primitive正规式有88项，限制真实左collar后为12个单字；全部非局部字与外部左多项式余项均为零。它准确给
$$
\begin{aligned}
n_2(u)=\int\bigl[
&u^2p^3-xup^4+\tfrac32x^2u^2pr^2+\tfrac3{10}x^2p^5\\
&-\tfrac12x^3u^2r^3-3x^3up^2r^2+\tfrac32x^4upr^3+\tfrac32x^4p^3r^2\\
&-\tfrac14x^5ur^4-x^5p^2r^3+\tfrac5{16}x^6pr^4-\tfrac3{80}x^7r^5
\bigr]\,dx .
\end{aligned}
$$
完整 Euler 多项式有24项，不是只保 principal。其 $u^{(4)}$ 系数可由显示密度 $L$ 手算为
$$
L_{rr}=3x^2(p-xr)\left(u-xp+\tfrac12x^2r\right)^2\not\equiv0.
$$
故存在真正紧光滑 profile 使 $n_2$ 非零；没有执行或声称找到某个实际 profile 数值见证。

$J_6$ 的整个primitive正规式有65项，但完整左表达全部抵消，局部、非局部及 Euler 表均为空，所以其零结论是全函数身份，不是一个测试族上的零。

原输入 $H_*$ mixed SHA c556d1a99522bb8cdc828d38ff00c8121ecaf7ad02dfe36861d26c547fb2ba76，diagonal c181256a91943ff0df4474737cf097e91cfcf3851810bdeac62047da982df298；$J_6$ mixed 432254370e395477f7636d7f16348a4d3467ffd11b8189a8d249ec813596724e，diagonal 163cb66d73959b8db6023525e5cb07755346950b7a4b8d7cb5ec9c17c16a74dd，均同已付源。

## 3. 与原商结论的接口

[R404](../results/R404-natural-weight-zero-image-at-most-two-and-single-function-kernel-criterion.md)的原关系 $n_4=-c_0n_6$ 因而给 $n_4=0$，不需要再求未知 $c_0$。完整自然权零像现在恰为 $\operatorname{span}(n_2)$，维数1；原联合核中 $\lambda_+=1$ 的代表不存在。

此处不把 signed 成本空间的结论冒为整个主课题不可能，也不把“所有紧 profile 的自然函数恒零”与“当前有限实际 profiles 的必要通量为零”混同。完整正字符下降和实际范围另写正式结果；当前 finite ordered totals、同包/跨包内部条件与同一个二阶规范继续研究。

## 4. 新人工与实际费用

八项人工全部通过：精确main framing；新外通量号及五次Euler；完整有序非局部余项；五次全导数Euler；最高导数；原右锚；真伸缩权；两函数比例/零分母/未决边界。没有执行旧开发套件，人工不读研究数据、不联网。

| 项目 | 实际值 |
|---|---:|
| 新人工 | 8/8通过 |
| 人工墙钟 | 0.008901954000009482秒 |
| 人工RSS | 32172KiB |
| 原报告只读与来源核对 | 1.6994761469999844秒 |
| 必要2个static、6个response输入恢复 | 4.239038563999998秒 |
| 两个完整新Ω映射 | 0.7124086469999611秒 |
| 科学进程总墙钟 | 6.6566286460000015秒 |
| 科学RSS | 114136KiB |
| 新primitive calls | 458 |
| 新cache峰值 | 1586项 |
| shuffle calls / cache | 9 / 9 |
| 最大word长度 | 3 |
| cycle fallback | 0 |
| 旧pure/self/Euler/秩/forcing/profile重执行 | 全部0 |

必要输入恢复保原SHA，只恢复新观察实际需要的2+6根。literal monitor的10次检查和maximum_integer_bits=0不冒整个DAG算术计数；完整新word统计如上。没有把旧研究费用列成本次新费用。

## 5. 输出身份及规则同步

| 原内容 | 字节 | SHA256 |
|---|---:|---|
| 完整job日志 | 123807 | fffe1b37deb54839af548cd50b155b956c4338744490f02668f8967f239ceda2 |
| 新人工JSON+LF | 15799 | 178ae038bf708e2afbba1069a28e65063c3ead5c6fb4956fa341bc78c8b79436 |
| 新科学JSON+LF | 31231 | 776e3f3fbe1872c877018a5b22a792203eac09265d589391d59223b7c11f758c |
| $H_*$完整Euler表 | 原报告内 | 5f663db9acab1b881d3727972732a254b0ef5206699d03a3d41614617acb5c97 |
| $H_*$完整左字表 | 原报告内 | bf502add6a272e2e9d05d7764fca3272e00c3235dab2ea40f1abbc36c8bf66cd |

规则15：这里保存人类结论、脚本、参数和来源hash；原日志及可重算JSON、字表不写Git、Release、artifact或跨run缓存。

本次实际公开 git pull --rebase 于23:39:53.121599—23:39:54.663555 UTC，从 d47749f7289ba0965e912a0e0e026bc619ebd4cb 到 3953c750413682d7b494c96f22e3546da741738d；根21bd547f56590b7f2dd279d0297efb289a9b2783、题d0432faff569c8e9af7ed4809847e12880976c11均空diff。随后detach到上述请求source执行，未把pull后的别题提交冒成执行source。

私有实际pull于23:39:56.440610—23:39:56.907262 UTC，前后均 ca2c85b5b4fce2e7a8a1968d10eda275ccd8e345；根5ba164843b1f5802184178a82d786264404873a3无变化，题README不存在，QUEUE仍是本会话唯一进行中。根于23:41:13读取以上回执并核差；下一实际公开pull最迟2026-11-16 00:39:53 UTC。
