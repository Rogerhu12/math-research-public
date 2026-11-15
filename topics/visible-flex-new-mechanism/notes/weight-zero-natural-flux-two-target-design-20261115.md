# 两条权零完整自然通量的新观察设计

日期：2026-11-15。**下一次公开 Actions 的源码与参数设计；尚未执行新开发检查或研究。** 不在本地导入、语法运行、求积、生成原根或执行符号归约。

## 1. 唯一新问题

R316、R333 已给同一个实际完整成本空间中的两个代表
$$
\begin{aligned}
H_*={}&C_2+\frac{649}{768}R_2-\frac{73}{3072}R_3
+\frac{649}{1536}R_4-\frac{821}{768}R_5
+\frac1{64}R_7+\frac{187}{1024}R_9,\\
J_6={}&C_6-\frac5{384}R_2+\frac5{1536}R_3
-\frac5{768}R_4+\frac1{384}R_5+\frac1{512}R_9.
\end{aligned}
$$
下标全部是 R126 **原 old 列号**，不是紧缩位置。已有
$$
\pi H_*=\pi J_6=0,\qquad
\mathcal Q(H_*)=\mathcal Q(J_6)=0,\qquad \lambda_+(H_*)=1.
$$
这些既有 universal 身份本次只读原报告，不重新证明或求秩。

新目标仅为
$$
n_2(u)=\Lambda_u(H_*),\qquad n_6(u)=\Lambda_u(J_6).
$$
由 R344 的完整 natural 定义与上述 pure 零，二者准确等于
$$
\Lambda_u(V)=\Omega_u(V)=\int u'''(x)V(u^2,0)(x)\,dx.
$$
没有从完整左二次 self $\mathcal Q=0$ 推出 $\Omega=0$。

R404 把原权零 natural 像降到 $\operatorname{span}(n_2,n_6)$；本次有用的联合判据是 $n_2\in\operatorname{span}(n_6)$。即使函数身份成立，本脚本也不宣称新增实际正锥、全 affine 字段或整个 period/gauge 已付。

## 2. 原 mixed 根到完整新观察的规范

对原 mixed Fourier 系数 $M_{-2}(q,\bar q)$，全局置 $\bar q=q=u$。原 $\theta=0$ 身份给
$$
V(u^2,0)=-4M_{-2}(u,u),\qquad
\Omega_u(V)=-4\int u'''M_{-2}(u,u).
\tag{1}
$$
源码的 primitive 是 $I_r^x(a)=\int_r^x a=-J(a)$。因此准确执行
$$
\boxed{\Omega_u(V)=4[I_r^x(u'''M_{-2}(u,u))]_{\rm left}.}
\tag{2}
$$
先对**整个**原表达式作两色识别，再新增乘 $u'''$ 和一次同锚积分；最后才使外部 local jets 在左 collar 为零。内部 primitive、嵌套增量、原 $N_0$、参考 $\Gamma$ 和真实左常数均保在原 DAG 中。

不改变右锚、不用另一支撑端替锚、不假内层输出紧，也不使用一条有限平端多项式 profile。多字输出仍是完整有序函数。

## 3. 原输入严格限定为两根加六列

### 3.1 两个完整 static 输入

$C_2,C_6$ 是 R196 同一 $\Gamma$ 的真权零 mixed $-2$ 原根：

| 输入 | 状态顺序 $(h,k,\omega,\log h)$ | 原 SHA256 |
|---|---|---|
| $C_2$ | $(0,2,0,0)$ | b2112caa38759e16999c782934dadf09f11770f4deb24938b22ae21e9640702f |
| $C_6$ | $(1,1,1,0)$ | 5ca598f50107cf8f059608f27694ad87bb5cbd26be152ff18d8d0f2e2a95bc02 |

原参考数据 SHA：c6276335dd47380509870798123478dc1b5a25ad83f3eef15d30cedcef4ece0b。

沿已发表 combine_normalization_rows 读取197个 static source records 的元数据，形成**只有这两个**必要原组合，再作其原真权零投影，逐结果核 R196 原 SHA。不重编 normal head、十四族、forcing 或 potential；$N_0$ 已在完整根中，不能省。

原输入位于 topic/notes/actions-43645177423-1-local_fourth_quotient：

- run43645177423，source2f1b809c0b0abb7a26303d36940edc203815f872；
- local-fourth-quotient.json：3982B，19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a；
- receipt SHA：c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba；
- local-fourth-quotient-original-expressions.json.gz：657195B，ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace；
- raw3518194B，d74e87790a00a246e01438c54575c3190389e3adbdefed0cec233b6ec9a664d1。

旧 producer 状态仍是原 output_limit；只使用它已完整导出的 W/static source，不将旧运行改称 complete。gzip 仅在 runner 内存读取。

### 3.2 六条必要响应

| R126 old 列 | quadratic | W index |
|---:|---|---:|
| 2 | p1 | 1 |
| 3 | p1 | 12 |
| 4 | p1 | 16 |
| 5 | p1 | 35 |
| 7 | p2 | 6 |
| 9 | p2 | 14 |

仅解码这些 W 和两目标实际需要的原根。R126 没有 portable response DAG，后来的 metadata-only 运行也未保 raw roots，故用已付 mixed_response 公式恢复六个 $-2$ 输入一次，逐条核原 SHA。其余十条 retained response、pure $-4$ 均不恢复。

R126 定义输入位于 topic/notes/actions-43649525432-1-g_first_translation：

- run43649525432，source5852d7d4400859e53dde789b4d63f200d0e0acce；
- G-first-translation.json：23923B，9926a1f7026064c95c297b34da60ed5f1b345bc37753a23e75295cf44792fe82；
- receipt33085B，06e5d82a7e7db8922d42347920609c83a3ad0114050cdbbdafc72084c3e25bec；
- G-first-translation-complete-report.json.gz：17734B，511431508d58a1b6fe3fb783efe6d9c0b9be9005c86c08796d992ad19441a30b；
- raw74559B，4f88bc5fa5af321c57953c1eb7316efbd53d7f4d2da21d2b9c933bcaf617ab45。

reader 中现存的原维数/依赖 hash 检查只验证来源，不重新执行这些秩或查询。

## 4. 已付身份的原 run/job/log

只读原完整日志中的精确科学 MAIN，不读取旧 self 列后再求解。

| 项目 | $H_*$：R316 | $J_6$：R329/R333 |
|---|---|---|
| run | 43735872441 | 43740129876 |
| job | 132878270740 | 132891272196 |
| source | ca186db057ed753abe565d0c3c2c8305278b5af7 | a5383f62d353890cc24e927b669dd2d6b67f8c78 |
| main字节 | 61441 | 37516 |
| main SHA | 731ffae43cc8f06346801c444a7de010fe2cf6f9f05ecf4b650d319fa2ee06fd | d4c5709c150392118ea0189be0f2114e52e9511df12d90f139836cace3863ca3 |
| receipt字节 | 55780 | 56025 |
| receipt SHA | 8d79ddda157153788ae70bb1cc44d6c64d4672541bb2e66f7cfbaf33f9549701 | 2854aecf26a0abf3b013d0674965315a3ba1702c681b76cf7f9ba1ba32947004 |
| 整job log字节 | 182877 | 136609 |
| 整job log SHA | 4d658489abd694f9f4cde2204aec9d23dc507d9ebae47168e42123cf4ff1288f | 6808d07a3ed6b20d503691de9c979ab5accd9526f52861906c4196ff53d49758 |

原只读 HTTP reader 不向签名日志 host 转发 API credential。核实际 run/job 的 complete/success、source和lane，再核整个log及原 MAIN JSON+LF。

同一日志还有 development COMPLETE_REPORT，故按精确 MAIN bytes/SHA筛选，不要求全部 tag 唯一；精确 MAIN 重复则拒绝。随后读原 MEMBER、universal pure/self 零、准确原响应组合和 fresh 原差 hash，并核原 source 递归叶与 receipt。

新实际输入必须再次匹配：

| 输入 | mixed复合 SHA | 原同色diagonal SHA |
|---|---|---|
| $H_*$ | c556d1a99522bb8cdc828d38ff00c8121ecaf7ad02dfe36861d26c547fb2ba76 | c181256a91943ff0df4474737cf097e91cfcf3851810bdeac62047da982df298 |
| $J_6$ | 432254370e395477f7636d7f16348a4d3467ffd11b8189a8d249ec813596724e | 163cb66d73959b8db6023525e5cb07755346950b7a4b8d7cb5ec9c17c16a74dd |

不以纸面抄录替代原收据，不因 self=0 删整个 mixed 函数。

## 5. 完整同锚 word 输出

沿 R178 PriorityWords，只将声明 profile degree 从四升到五，颜色固定为真实 q。strict descent、完整 shuffle、三角对角项和非空word的多项式边界均沿原规则。这是两个新五次泛函的必要归约，不单独重新映射旧 quartic/class/rank。

完整左表达写成
$$
\sum_{p\ge0}x^p\sum_w c_{p,w}I_w.
$$
若仍有 $p>0$ left-polynomial关系或任意多字，原表完整输出 unresolved，不删弃、对称化或当作非成员证据。

单字规范：
$$
cI_r^x(x^p\prod u^{(j)})|_{\rm left}
=-c\int x^p\prod u^{(j)}.
$$
所以局部密度 coefficient 是单字 coefficient 的负数；多字继续用原 signed-I 规范。

成本真权零对应总通量 profile 伸缩权 $-2$。逐字用全部 $x$ 幂、导数阶和 primitive 数检查，不沿用左二次 self 的不同提取公式。

## 6. 全部局部后才用忠实 Euler

如果完整(2)成为
$$
\Omega(u)=\int L(x,u,\ldots,u^{(m)}),\quad L\text{ 齐次五次},
$$
计算**整个**
$$
\mathscr E(L)=\sum_{j=0}^m(-D_x)^j\frac{\partial L}{\partial u^{(j)}}.
$$
所有高低项全输出，不能只取 principal。对紧 u，齐次恒等及真实端 jets 给
$$
5\int L=\int u\,\mathscr E(L).
\tag{3}
$$
Euler 字面零足以推普遍零。反向若泛函对全部紧 u 都零，任意紧变分和 fundamental lemma 给 Euler 在每个u上零，再由自由内点jets得到多项式字面零。故此完整局部类中判据充分且必要，不依赖word NF完备。

只在两目标均完整局部时比较两个新 Euler：

- $E_6=0$ 时，$n_2\in\operatorname{span}(n_6)$ iff $E_2=0$；
- $E_6\ne0$ 时，从首个非零系数得唯一比例候选，再逐项检查 $E_2-cE_6$；
- 差零给全函数比例，差非零给这两个完整局部泛函独立；
- 任一仍有非局部或left-polynomial，关系保持 unresolved。

这里没有恢复旧比较空间或重做旧秩。若 Euler 非零，结论是存在真实紧 $C^\infty$ profile 见证；脚本不声称已经构造或评价该 profile。

## 7. 源码、请求与首次执行

单新入口为 scripts/literature_weight_zero_natural_flux.py，冻结 42478 B，
SHA256 be12b9338cf5558eacb4d05b43f201871fae5d4262dd330304eaa56df3c2e12f。

原31文件科学 source 闭包均沿 R329 冻结 SHA，加新入口共32 bindings，完整列在 request。入口逐文件核对；旧 R329 source_identity 为原 input reader提供冻结producer/source树，只读源码身份，不调用旧研究或人工。

CLI：--request PATH --out PATH。另加 --development 仅作新人工。
建议 request：computations/request-weight-zero-natural-flux.json。

root 独占 workflow、实际pull/read、规则同步、publisher和refs。本稿不触发运行。输出临时JSON完整打印 COMPLETE_REPORT，另打印bytes/SHA。原log、gzip、可重算输出与证书不写入仓库、Release或artifact。

## 8. 八项仅新增的公开人工

首次执行仅在新public Actions，没有本地运行：

1. 同schema development跳过、精确main framing与重复拒绝；
2. 人工 $M=-u^4/4$ 给 $\Omega=6\int u^2u'^3$，并核五次Euler号；
3. 人工 $M=-u^2I(u''^2)/4$ 保完整 $3+2$ 有序字及真负号；
4. 五次 total derivative 的完整Euler零；
5. $u^3u'''^2$ 的第六导数项不删；
6. 新Ω保原右零边界恒等，不重置左端；
7. 错true-weight标签拒绝；
8. 新两Euler比例、零分母、独立与非局部unresolved边界。

人工不读科学根/数据、不联网、不执行旧套件。R316十二项、R329八项、R342十项不重跑。

## 9. 预算与分账

| 项目 | 上限 |
|---|---:|
| 必要输入恢复和新科学wall | 120秒 |
| RSS | 512MiB |
| 有理整数位数 | 8192 |
| 单表达项 | 100000 |
| 新共享primitive calls | 300000 |
| 新缓存项 | 250000 |
| 主输出 | 95000B |
| 单个原job只读log | 8MiB |

分开记录旧报告读取、必要2+6输入恢复、两次新映射耗时。literal monitor明确不冒所有DAG算术；新word stats/calls、RSS、原source/inputhash全保。

预算/语法/输入不一致即停止，没有自动加预算或换profile族。完整表达输出超限只报大小/hash及 complete_formula_output_limit，不从截断输出发数学决定。正常多字余项是已完成观察但数学 unresolved，完整有限式交纸推。

| 项目 | 本次 |
|---|---:|
| 新完整Ω映射 | 2 |
| static mixed必要恢复 | 2 |
| response mixed必要恢复 | 6 |
| 旧pure根/查询/normalization | 0 |
| 旧self/T/Euler映射 | 0 |
| 旧十三列/旧7秩/H0秩实验 | 0 |
| forcing/新N投影 | 0 |
| profile族评价/求积/扫描 | 0 |
| 旧人工 | 0 |

## 10. 准确后续边界

输出应是两条原完整函数的明示同锚word身份，以及完全局部时的忠实Euler决定，不再只得到一条profile族上零。

若有 $n_2=cn_6$，可用 $H_*-cJ_6$ 作为 $\ker(E,\Lambda_{\rm all})$ 的具体线性代表继续纸推；若独立，R404相应权零kernel条件确有障碍。任一结果都不把signed代表当实际路径，不自动合并分开截面，也不删除共同右尾、整包通量、内部退化、平台、全局连接与同一个二阶gauge十三门。
