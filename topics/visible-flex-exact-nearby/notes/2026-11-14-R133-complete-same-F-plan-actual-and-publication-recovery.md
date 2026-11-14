# R133：完整矩阵计划的实际七门与发布层恢复

公开 run [43651733856](https://github.com/Rogerhu12/math-research-public/actions/runs/43651733856) 的 plan 数学子进程已经退出 0，7 门全部通过。它完成原 5970 格 cover、所有共享 Q 与 R 端点、原四格同 F 完整 15 门及其数组 SHA、32 组共 5966 个缺格的互斥计划核验。随后 CI 在写小摘要时执行 PosixPath 加字符串，抛出 TypeError；因此整个 run 为 failure，32 个 range 与 finish 都 skipped，尚无任何新的全矩阵格。

## 原样证据

目录：

notes/complete_same_F_directional_matrices_ci/run-43651733856-1-complete-same-F-plan/

| 原文件 | 字节 | SHA256 |
|---|---:|---|
| process.json，公开仓库快照 | 7212 | 98fca8dad6990772d6a99eee4bf3a4e489bdbc36646c7c81fd90af3be9ca4736 |
| evidence/actual-latest-matrix-outcome.json | 1436 | 2e5002b595fa8737df2b8732982e264a6f4a0e0e717a4cc254ad03933d97a6fd |
| native/complete-exact5970-same-F-disjoint-plan.json.gz | 266218 | d893f609bc12e58720444b99a565dc5fdb79df1842cdab4ba6da3ac695a46fd4 |

实际数学 label 为 exact_full5970_matrix_plan_and_four_original_same_F_receipts，child wall time 为 5.000476093000003 秒，actual_returncode=0。source SHA256 为 47d69d780b701953561df7eff0d425745577bfbaa9b4a865d8d8cf5c2f9056c6；原 CI SHA256 为 4ba644699fcf2a531682c54be924eea8d8d5e03efd9376bb80366b7ecf53cbc7；原 117 件 manifest 为 a9e1b1646031d1cfdb3472570228920730e8a3736819a257746a2960138e50fc。原 artifact 14136022666 实际为 4076089 字节，包含真实过程、计划 native、原 profile 与全部已保存证据。

原过程准确保留 complete=false 及异常：

`unsupported operand type(s) for +: 'PosixPath' and 'str'`。

失败位置为原 CI 的小摘要路径拼接，发生在数学完成并保存 native 之后。不能把它写成数学门失败，也不能因此重算完整原计划。

## 修复与接续

独立 v2 worker 只修摘要路径为完整 f-string Path 段，并明确接受上述唯一原 run/attempt、原 worker/manifest、精确 process SHA、原 native SHA、实际 child0 与全部七门一致的成功计划。旧 process.complete=false 和原错误不改写。新 worker 的成功复用记录给出原过程和原 native 的 SHA，不把新过程伪称原 artifact 过程。

原科学 source、合同与全部原 117 个文件 SHA 均保留。v2 使用新 worker、manifest 和 workflow 路径，旧 workflow 不会因此次 push 自动重跑。新的 plan 阶段恢复原 native 字节而不再次启动数学子进程；之后只执行原互斥计划的 5966 个缺格。原四格矩阵、原 5970 reference/validator 和任何 target 均不重算。

本次实际 plan 的 4 次真 pull/README 差异检查均为空；最后已读提交为 da0ecd856291b2ae77e0c78c567f7cac31ff851e，独立规则审阅提交仍为 ee26c0a65a2e63c15f2ccfba6714181584416542。该计划与恢复记录不授全矩阵方向 Green 或无限 PDE 逆。
