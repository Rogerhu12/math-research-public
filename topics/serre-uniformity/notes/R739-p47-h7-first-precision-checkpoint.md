# R739 原 p47/h7：首个完整有限计数及模 p4 检查点

2026-11-14。公开 run [43609325075](https://github.com/Rogerhu12/math-research-public/actions/runs/43609325075)
已完成全部原有限计数和模 $47^4$ 求和，job132490689367 全部步骤成功，
source fd54e412b675291cd86d91df401d3e030e4eeca8。

实际且唯一允许登记的精度结论为
$$
N_7\equiv0\pmod{47^4},\qquad v_{47}(N_7)\ge4.
$$
原 $N_7\ne0$ 的理论输入仍见 R727；本精度没有确定准确赋值、奇偶或
$M_{2,7}$ 的准确赋值。不能把零模结果四舍五入为赋值四。

全部 $47$ 条原 torus 行、$48$ 个字符计数、Teichmüller 生成元、
原向量 $e_0$、共轭对称及每个模 $47^4$ 加项均已保存。
正式完整计数只用时 0.3624198040000053 秒（含读取规则步骤）。
后续只需使用原已存计数做精确圆分化简或增加 Teichmüller 精度，
不得重枚举原纤维。

## 原凭据

相对路径基址：
[computations/R739-original-finite-norm-p47-h7/43609325075-1/](../computations/R739-original-finite-norm-p47-h7/43609325075-1/)

| 文件 | SHA256 |
|---|---|
| R739-p47-h7-exact-N.json | 33afb0aad5f900baea0cb881a888e44815e2caad504633daed576812506fab88 |
| R739-fiber-checkpoint.json | eb805a0fe9fdd6404a5e75cba77fdef0084ff85b94874565cfdd471841c49e5f |
| R739-p47-h7-original-fibers.json.gz | e01a1fda63168d8d32124199b06bf5627cb2ce68911eccaf8fb5ab3bdd0daa01 |
| run-receipt.json | 251b98e0a0df8f973ff26d14e0d76a9a2e05a24cab63fde62a2620a9fc611a58 |
| public-actions-input.json | 12bf7aeda4dddbed5b83f928076edc4ca70802e04b1b40b6d19fb1897f3c5377 |
| R739-readme-check.json | eae325ba538536bb34208bfb4b203cd5e7f328dfb17532f5df8e57f9832f098b |

完整 artifact 为 serre-cartier-R739-original-finite-norm-p47-h7-43609325075-1，
ID14119179449，21572 bytes，zip SHA256
7eef15b761c93b007d44af3ff7f09aac4febf79cc70123884477632021b65b21。
它保留同一源码、请求、工作流、两 README 和全部失败/检查接口。
源码 SHA256 为
a18c040311e13990b46523943d44aadb937c129a84987b3333830be2ff61954d。

发布器在 15:17:10.6439663 UTC 实际执行完
git pull --rebase origin main，随后再次比较两 README，无差异，
于 15:17:11 UTC 推送原输出。该次实际 pull 不是集成只读核查。
手工会话终端仍不可用；下次实际 pull 不晚于 16:17 UTC。

本条是已完成的精确有限精度结论；R739 的准确赋值问题仍继续。
